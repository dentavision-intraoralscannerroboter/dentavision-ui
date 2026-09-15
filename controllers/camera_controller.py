from __future__ import annotations

import cv2
from PySide6.QtCore import QTimer
from PySide6.QtGui import QPixmap

from ui.rounded_video_label import RoundedVideoLabel, RED_DOT_Y_AXIS
from ui.frame_display import to_pixmap
from ui.status_labels import set_face_detected, set_face_not_found
from vision.camera import Camera
from vision.face_tracker import FaceTracker, compute_face_bbox, compute_mouth_bbox, mouth_corner_points
from vision.frame_annotation import draw_face_box, draw_mouth_box, draw_face_not_found
from vision.head_pose import estimate_head_position, estimate_head_orientation, check_stabilization

STABILIZATION_TOLERANCE_PX = 15

CM_PER_PIXEL = 0.025
MM_PER_PIXEL = CM_PER_PIXEL * 10


class CameraController:

    def __init__(
            self,
            parent_frame,
            header_label,
            face_status_label=None,
            stabilization_successful_label=None,
            head_not_stabilized_label=None,
            scanning_label=None,
            on_tracking_lost=None,
            on_tracking_restored=None,
            head_position=None,
            on_head_position_updated=None,
            interval_ms: int = 30
        ):
        self.video_label = RoundedVideoLabel(radius=14, parent=parent_frame)
        self._position_label(parent_frame, header_label)

        self.face_status_label = face_status_label
        self._face_detected_state: bool | None = None

        self.stabilization_label = stabilization_successful_label
        self.head_not_stabilized_label = head_not_stabilized_label
        self._stabilization_state: str | None = None

        self.scanning_label = scanning_label
        self._scanning_active: bool = False

        self.on_tracking_lost = on_tracking_lost
        self.on_tracking_restored = on_tracking_restored
        self._selection_ok_state: bool | None = None

        self.head_position = head_position
        self.on_head_position_updated = on_head_position_updated

        self.camera: Camera | None = None
        self.tracker: FaceTracker | None = None

        self.timer = QTimer()
        self.timer.timeout.connect(self._update_frame)
        self.interval_ms = interval_ms

    def _position_label(self, parent_frame, header_label) -> None:
        margin = 10
        top = header_label.geometry().bottom() + margin
        self.video_label.setGeometry(
            margin,
            top,
            parent_frame.width() - 2 * margin,
            parent_frame.height() - top - margin,
        )
        self.video_label.show()

    @property
    def face_detected(self) -> bool:
        return bool(self._face_detected_state)

    @property
    def stabilized(self) -> bool:
        return self._stabilization_state == "stabilized"

    def check_ready(self, action: str) -> bool:
        if not self.face_detected:
            print(f"Cannot {action}: face not detected")
            return False
        if not self.stabilized:
            print(f"Cannot {action}: head not stabilized")
            return False
        return True

    def start_scanning(self) -> bool:
        if not self.check_ready("start scanning"):
            return False
        self._scanning_active = True
        if self.scanning_label is not None:
            self.scanning_label.show()
        return True

    def pause_scanning(self) -> None:
        self._scanning_active = False

    def _set_face_status(self, face_found: bool) -> None:
        if self.face_status_label is None or self._face_detected_state == face_found:
            return
        self._face_detected_state = face_found
        if face_found:
            set_face_detected(self.face_status_label)
        else:
            set_face_not_found(self.face_status_label)

    def _set_stabilization_status(self, state: str) -> None:
        if self._stabilization_state == state:
            return
        self._stabilization_state = state

        if state == "stabilized":
            if self.stabilization_label is not None:
                self.stabilization_label.show()
            if self.head_not_stabilized_label is not None:
                self.head_not_stabilized_label.hide()
        elif state == "not_stabilized":
            if self.stabilization_label is not None:
                self.stabilization_label.hide()
            if self.head_not_stabilized_label is not None:
                self.head_not_stabilized_label.show()
        else:
            if self.stabilization_label is not None:
                self.stabilization_label.hide()
            if self.head_not_stabilized_label is not None:
                self.head_not_stabilized_label.hide()

    def start(self) -> None:
        if self.camera is not None:
            return
        self.camera = Camera()
        self.tracker = FaceTracker()
        self._set_face_status(False)
        self._set_stabilization_status("hidden")
        self.timer.start(self.interval_ms)

    def stop(self) -> None:
        self.timer.stop()
        if self.camera is not None:
            self.camera.release()
            self.camera = None
        self.tracker = None
        self.video_label.setPixmap(QPixmap())
        self.video_label.setText("Camera off")
        self._set_face_status(False)
        self._set_stabilization_status("hidden")

        if self._scanning_active:
            self._scanning_active = False
            if self.scanning_label is not None:
                self.scanning_label.hide()
            print("Scanning Paused")

    def _update_frame(self) -> None:
        frame = self.camera.read_frame()
        if frame is None:
            self.stop()
            return

        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_frame.shape

        results = self.tracker.face_mesh.process(rgb_frame)

        if results.multi_face_landmarks:
            self._set_face_status(True)
            landmarks = results.multi_face_landmarks[0]

            x_min, y_min, x_max, y_max = compute_face_bbox(landmarks, w, h)
            draw_face_box(rgb_frame, x_min, y_min, x_max, y_max)

            mouth_x_min, mouth_y_min, mouth_x_max, mouth_y_max = compute_mouth_bbox(landmarks, w, h)
            draw_mouth_box(rgb_frame, mouth_x_min, mouth_y_min, mouth_x_max, mouth_y_max)

            mouth_mid_x = (mouth_x_min + mouth_x_max) // 2
            mouth_mid_y = (mouth_y_min + mouth_y_max) // 2

            target_x = w // 2
            target_y = int(h * RED_DOT_Y_AXIS)

            self._set_stabilization_status(
                check_stabilization(mouth_mid_x, mouth_mid_y, target_x, target_y, STABILIZATION_TOLERANCE_PX)
            )

            mouth_width_px = mouth_x_max - mouth_x_min

            if self.head_position is not None and mouth_width_px > 0:
                mouth_left_x, mouth_left_y, mouth_right_x, mouth_right_y = mouth_corner_points(landmarks, w, h)

                x_mm, y_mm = estimate_head_position(
                    mouth_mid_x, mouth_mid_y, target_x, target_y, MM_PER_PIXEL
                )
                rx, ry, rz = estimate_head_orientation(
                    mouth_left_x, mouth_left_y, mouth_right_x, mouth_right_y,
                    mouth_mid_x, mouth_mid_y, x_min, x_max, y_min, y_max,
                )

                self.head_position.detected = True
                self.head_position.x = x_mm
                self.head_position.y = y_mm
                self.head_position.rx = rx
                self.head_position.ry = ry
                self.head_position.rz = rz

                if self.on_head_position_updated is not None:
                    self.on_head_position_updated()

        else:
            self._set_face_status(False)
            self._set_stabilization_status("hidden")
            if self.head_position is not None:
                self.head_position.detected = False
            draw_face_not_found(rgb_frame)

        if self._scanning_active and not (self.face_detected and self.stabilized):
            self._scanning_active = False
            if self.scanning_label is not None:
                self.scanning_label.hide()
            print("Scanning Paused")

        selection_ok = self.face_detected and self.stabilized
        if self._selection_ok_state is not None:
            if self._selection_ok_state and not selection_ok:
                if self.on_tracking_lost is not None:
                    self.on_tracking_lost()
            elif not self._selection_ok_state and selection_ok:
                if self.on_tracking_restored is not None:
                    self.on_tracking_restored()
        self._selection_ok_state = selection_ok

        self.video_label.setPixmap(to_pixmap(rgb_frame, w, h, ch))