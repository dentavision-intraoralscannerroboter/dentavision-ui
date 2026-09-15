import cv2

TEAL_RGB = (20, 70, 190)
FACE_LINE_THICKNESS = 3
MOUTH_LINE_THICKNESS = 3


def draw_face_box(frame, x_min: int, y_min: int, x_max: int, y_max: int) -> None:
    cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), TEAL_RGB, FACE_LINE_THICKNESS)
    cv2.putText(frame, "FACE DETECTED", (x_min, y_min - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, TEAL_RGB, FACE_LINE_THICKNESS)


def draw_mouth_box(frame, x_min: int, y_min: int, x_max: int, y_max: int) -> None:
    cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), TEAL_RGB, MOUTH_LINE_THICKNESS)
    cv2.putText(frame, "MOUTH", (x_min, y_min - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, TEAL_RGB, MOUTH_LINE_THICKNESS)


def draw_face_not_found(frame) -> None:
    cv2.putText(frame, "Face not found", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, TEAL_RGB, FACE_LINE_THICKNESS)