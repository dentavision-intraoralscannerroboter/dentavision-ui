import sys
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication, QMainWindow
from ui.mainwindow_ui import Ui_MainWindow
from ui.buttons import style_start_button, set_start_text, set_scan_text, set_pause_text
from ui.status_labels import (
    set_aligning,
    set_target_reached,
    set_scanning_active,
    set_scanning_successful,
    set_paused,
)
from ui.stabilization_error_label import build_stabilization_error_label
from controllers.dental_chart_controller import DentalChartController
from controllers.tooth_badge_controller import ToothInfoController
from controllers.camera_controller import CameraController
from controllers.tooth_target_controller import ToothTargetController
from controllers.joint_motion_controller import MotionController
from core.models import HeadPosition

STATUS_LABEL_DELAY_MS = 2000


class ControlPanel(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.stabilizationSuccessfulLabel.hide()
        self.ui.scanningLabel.hide()
        self.ui.headIsNotStabilizedLabel.hide()
        self.ui.jointsAreMovingLabel.hide()

        self.target_reached_timer = QTimer(self)
        self.target_reached_timer.setSingleShot(True)
        self.target_reached_timer.timeout.connect(self._show_target_reached)

        self.scanning_successful_timer = QTimer(self)
        self.scanning_successful_timer.setSingleShot(True)
        self.scanning_successful_timer.timeout.connect(self._show_scanning_successful)

        self.ui.startButton.clicked.connect(self.on_start_clicked)
        style_start_button(self.ui.startButton)
        self._phase = "idle"
        self._target_reached = False

        self.stabilization_error_label = build_stabilization_error_label(self.ui.centerPanel)

        self.head_position = HeadPosition()
        self.tooth_info = ToothInfoController(self.ui)
        self.tooth_target = ToothTargetController(self.ui, self.head_position)
        self.tooth_chart = DentalChartController(
            mouth_frame=self.ui.mouthFrame,
            on_tooth_selected=self.on_tooth_selected,
            can_select=self.can_select_tooth,
        )
        self.motion_control = MotionController(self.ui.motionControl)

        self.camera = CameraController(
            parent_frame=self.ui.rightTopPanel,
            header_label=self.ui.headPositionLabel,
            face_status_label=self.ui.faceDetectedLabel,
            stabilization_successful_label=self.ui.stabilizationSuccessfulLabel,
            head_not_stabilized_label=self.ui.headIsNotStabilizedLabel,
            scanning_label=self.ui.scanningLabel,
            on_tracking_lost=self.on_tracking_lost,
            on_tracking_restored=self.on_tracking_restored,
            head_position=self.head_position,
            on_head_position_updated=self._on_head_position_updated,
        )
        self.camera.start()

    def on_start_clicked(self):
        if self._phase == "idle":
            if self.tooth_chart.selected_tooth is None:
                print("Cannot start: no tooth selected")
                return
            if not self.camera.check_ready("start"):
                return
            tooth = self.tooth_chart.selected_tooth
            x, y, z, rx, ry, rz = self.tooth_target.show_target_for(tooth)
            self.motion_control.set_baseline(x, y, z, rx, ry, rz)
            print("Joints are moving...")
            self._target_reached = False
            set_aligning(self.ui.jointsAreMovingLabel)
            self.ui.jointsAreMovingLabel.show()
            self.target_reached_timer.start(STATUS_LABEL_DELAY_MS)
            set_scan_text(self.ui.startButton)
            self._phase = "aligning"

        elif self._phase == "aligning" and not self._target_reached:
            print("Cannot scan yet: target not reached")

        elif self._phase in ("aligning", "paused"):
            self.target_reached_timer.stop()
            self.ui.jointsAreMovingLabel.hide()
            self.ui.motionControl.setEnabled(False)
            set_scanning_active(self.ui.scanningLabel)
            self.camera.start_scanning()
            self.scanning_successful_timer.start(STATUS_LABEL_DELAY_MS)
            set_pause_text(self.ui.startButton)
            self._phase = "scanning"

        elif self._phase == "scanning":
            print("Scanning paused for joint re-calibration")
            self._enter_paused()

    def _enter_paused(self) -> None:
        self.scanning_successful_timer.stop()
        self.camera.pause_scanning()
        self.ui.motionControl.setEnabled(True)
        set_paused(self.ui.scanningLabel)
        set_scan_text(self.ui.startButton)
        self._phase = "paused"

    def _show_target_reached(self):
        self._target_reached = True
        set_target_reached(self.ui.jointsAreMovingLabel)

    def _show_scanning_successful(self):
        set_scanning_successful(self.ui.scanningLabel)

    def can_select_tooth(self) -> bool:
        return self.camera.check_ready("select tooth")

    def on_tooth_selected(self, tooth):
        print(f"Tooth {tooth.number} is selected")
        self.tooth_info.show_tooth(tooth)
        self.tooth_target.show_target_for(tooth)

    def _on_head_position_updated(self):
        tooth = self.tooth_chart.selected_tooth
        if tooth is not None and self.camera.stabilized:
            self.tooth_target.show_target_for(tooth)

    def on_tracking_lost(self):
        print("Tracking lost")

        if self._phase == "scanning":
            print("Stabilization lost during scan — pausing automatically")
            self._enter_paused()
            self.stabilization_error_label.show()
            self.ui.startButton.setEnabled(False)
            self.tooth_target.clear()
            return

        self.tooth_chart.clear_selection()
        self.tooth_info.clear()
        self.tooth_target.clear()
        self.stabilization_error_label.show()
        self.ui.startButton.setEnabled(False)
        set_start_text(self.ui.startButton)
        self.target_reached_timer.stop()
        self.ui.jointsAreMovingLabel.hide()
        self.ui.motionControl.setEnabled(True)
        self._phase = "idle"

    def on_tracking_restored(self):
        self.stabilization_error_label.hide()
        self.ui.startButton.setEnabled(True)

    def closeEvent(self, event):
        self.camera.stop()
        return super().closeEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ControlPanel()
    window.show()
    sys.exit(app.exec())