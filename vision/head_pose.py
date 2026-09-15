import math

def estimate_head_position(
    mouth_mid_x: float,
    mouth_mid_y: float,
    target_x: float,
    target_y: float,
    mm_per_pixel: float,
) -> tuple[float, float]:
    x_mm = (mouth_mid_x - target_x) * mm_per_pixel
    y_mm = (target_y - mouth_mid_y) * mm_per_pixel

    return (x_mm, y_mm)


YAW_SCALE_DEG = 45.0
PITCH_SCALE_DEG = 45.0


def estimate_head_orientation(
    mouth_left_x: float,
    mouth_left_y: float,
    mouth_right_x: float,
    mouth_right_y: float,
    mouth_mid_x: float,
    mouth_mid_y: float,
    face_x_min: float,
    face_x_max: float,
    face_y_min: float,
    face_y_max: float,
) -> tuple[float, float, float]:
    rz = math.degrees(math.atan2(
        mouth_right_y - mouth_left_y,
        mouth_right_x - mouth_left_x,
    ))

    face_mid_x = (face_x_min + face_x_max) / 2
    face_mid_y = (face_y_min + face_y_max) / 2
    face_half_w = (face_x_max - face_x_min) / 2
    face_half_h = (face_y_max - face_y_min) / 2

    yaw_ratio = (mouth_mid_x - face_mid_x) / face_half_w if face_half_w else 0.0
    pitch_ratio = (mouth_mid_y - face_mid_y) / face_half_h if face_half_h else 0.0

    ry = yaw_ratio * YAW_SCALE_DEG
    rx = pitch_ratio * PITCH_SCALE_DEG

    return (rx, ry, rz)


def check_stabilization(
    mouth_mid_x: float,
    mouth_mid_y: float,
    target_x: float,
    target_y: float,
    tolerance_px: float,
) -> str:
    distance = math.hypot(mouth_mid_x - target_x, mouth_mid_y - target_y)
    return "stabilized" if distance <= tolerance_px else "not_stabilized"