FACE_DETECTED_TEXT = "● FACE DETECTED"
FACE_NOT_FOUND_TEXT = "●  FACE NOT FOUND"

FACE_DETECTED_STYLE = "color: #11AC00; font-weight: 600; font-size: 11px;"
FACE_NOT_FOUND_STYLE = "color: #C83C3C; font-weight: 600; font-size: 11px;"


def set_face_detected(label) -> None:
    label.setText(FACE_DETECTED_TEXT)
    label.setStyleSheet(FACE_DETECTED_STYLE)


def set_face_not_found(label) -> None:
    label.setText(FACE_NOT_FOUND_TEXT)
    label.setStyleSheet(FACE_NOT_FOUND_STYLE)


SCANNING_LABEL_STYLE = "color: #11AC00; font-weight: 600; font-size: 11px;"
PAUSED_LABEL_STYLE = "color: #C83C3C; font-weight: 600; font-size: 11px;"

ALIGNING_TEXT = "● JOINTS ARE MOVING"
TARGET_REACHED_TEXT = "● TARGET REACHED"
SCANNING_ACTIVE_TEXT = "● SCANNING..."
SCANNING_SUCCESSFUL_TEXT = "● SCANNING SUCCESSFUL"
PAUSED_TEXT = "● PAUSED"


def set_aligning(label) -> None:
    label.setText(ALIGNING_TEXT)


def set_target_reached(label) -> None:
    label.setText(TARGET_REACHED_TEXT)


def set_scanning_active(label) -> None:
    label.setText(SCANNING_ACTIVE_TEXT)
    label.setStyleSheet(SCANNING_LABEL_STYLE)


def set_scanning_successful(label) -> None:
    label.setText(SCANNING_SUCCESSFUL_TEXT)


def set_paused(label) -> None:
    label.setText(PAUSED_TEXT)
    label.setStyleSheet(PAUSED_LABEL_STYLE)