import mediapipe as mp
from core.models import HeadPosition

MOUTH_LANDMARK_IDS = sorted({idx for pair in mp.solutions.face_mesh.FACEMESH_LIPS for idx in pair})
MOUTH_BOX_PADDING = 6

MOUTH_LEFT_CORNER_IDX = 61
MOUTH_RIGHT_CORNER_IDX = 291


class FaceTracker:
    def __init__(self):
        self.face_mesh = mp.solutions.face_mesh.FaceMesh(
            static_image_mode=False,
            max_num_faces=1
        )

    def detect(self, frame) -> HeadPosition:
        results = self.face_mesh.process(frame)
        if not results.multi_face_landmarks:
            return HeadPosition(detected=False)

        landmarks = results.multi_face_landmarks[0]
        nose_tip = landmarks.landmark[1]

        return HeadPosition(
            detected=True,
            x=nose_tip.x,
            y=nose_tip.y,
            z=nose_tip.z
        )


def compute_face_bbox(landmarks, w: int, h: int) -> tuple[int, int, int, int]:
    xs = [lm.x * w for lm in landmarks.landmark]
    ys = [lm.y * h for lm in landmarks.landmark]
    return int(min(xs)), int(min(ys)), int(max(xs)), int(max(ys))


def compute_mouth_bbox(landmarks, w: int, h: int) -> tuple[int, int, int, int]:
    mouth_xs = [landmarks.landmark[i].x * w for i in MOUTH_LANDMARK_IDS]
    mouth_ys = [landmarks.landmark[i].y * h for i in MOUTH_LANDMARK_IDS]

    x_min = max(0, int(min(mouth_xs)) - MOUTH_BOX_PADDING)
    x_max = min(w - 1, int(max(mouth_xs)) + MOUTH_BOX_PADDING)
    y_min = max(0, int(min(mouth_ys)) - MOUTH_BOX_PADDING)
    y_max = min(h - 1, int(max(mouth_ys)) + MOUTH_BOX_PADDING)
    return x_min, y_min, x_max, y_max


def mouth_corner_points(landmarks, w: int, h: int) -> tuple[float, float, float, float]:
    left = landmarks.landmark[MOUTH_LEFT_CORNER_IDX]
    right = landmarks.landmark[MOUTH_RIGHT_CORNER_IDX]
    return left.x * w, left.y * h, right.x * w, right.y * h