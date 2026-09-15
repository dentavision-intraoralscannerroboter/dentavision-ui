# Tooth numbers (FDI notation), names, and Tooth Target offsets
import math

UPPER_TEETH = [18, 17, 16, 15, 14, 13, 12, 11, 21, 22, 23, 24, 25, 26, 27, 28]
LOWER_TEETH = [48, 47, 46, 45, 44, 43, 42, 41, 31, 32, 33, 34, 35, 36, 37, 38]

TOOTH_NAMES = {
    18: "Upper Right Third Molar", 17: "Upper Right Second Molar", 16: "Upper Right First Molar",
    15: "Upper Right Second Premolar", 14: "Upper Right First Premolar", 13: "Upper Right Canine",
    12: "Upper Right Lateral Incisor", 11: "Upper Right Central Incisor",
    21: "Upper Left Central Incisor", 22: "Upper Left Lateral Incisor", 23: "Upper Left Canine",
    24: "Upper Left First Premolar", 25: "Upper Left Second Premolar", 26: "Upper Left First Molar",
    27: "Upper Left Second Molar", 28: "Upper Left Third Molar",
    48: "Lower Right Third Molar", 47: "Lower Right Second Molar", 46: "Lower Right First Molar",
    45: "Lower Right Second Premolar", 44: "Lower Right First Premolar", 43: "Lower Right Canine",
    42: "Lower Right Lateral Incisor", 41: "Lower Right Central Incisor",
    31: "Lower Left Central Incisor", 32: "Lower Left Lateral Incisor", 33: "Lower Left Canine",
    34: "Lower Left First Premolar", 35: "Lower Left Second Premolar", 36: "Lower Left First Molar",
    37: "Lower Left Second Molar", 38: "Lower Left Third Molar",
}

ARCH_WIDTH_MM = 45.0
ARCH_HEIGHT_MM = 8.0
ARCH_DEPTH_MM = 20.0

UPPER_PITCH_OFFSET_DEG = -20.0
LOWER_PITCH_OFFSET_DEG = 20.0

PITCH_DEPTH_SCALE_DEG = 10.0

_UPPER_ANGLE_RANGE = (195, 345)
_LOWER_ANGLE_RANGE = (165, 15)


def _arc_offsets(tooth_numbers: list[int], angle_range: tuple[float, float], y_sign: int):
    start_angle, end_angle = angle_range
    count = len(tooth_numbers)
    offsets = {}
    angles = {}
    for i, tooth_number in enumerate(tooth_numbers):
        angle_deg = start_angle + (end_angle - start_angle) * i / (count - 1)
        angle_rad = math.radians(angle_deg)
        dx = ARCH_WIDTH_MM * math.cos(angle_rad)
        dy = y_sign * ARCH_HEIGHT_MM * abs(math.sin(angle_rad))
        offsets[tooth_number] = (dx, dy)
        angles[tooth_number] = angle_deg
    return offsets, angles


def _depth_fraction(offsets_2d: dict[int, tuple[float, float]]) -> dict[int, float]:
    abs_dx_values = [abs(dx) for dx, _dy in offsets_2d.values()]
    min_abs_dx, max_abs_dx = min(abs_dx_values), max(abs_dx_values)
    span = max_abs_dx - min_abs_dx
    return {
        tooth_number: (abs(dx) - min_abs_dx) / span
        for tooth_number, (dx, _dy) in offsets_2d.items()
    }


def _depth_offsets(depth_fraction: dict[int, float]) -> dict[int, float]:
    return {
        tooth_number: ARCH_DEPTH_MM * fraction
        for tooth_number, fraction in depth_fraction.items()
    }


def _rotation_offsets(
    tooth_numbers: list[int],
    angles: dict[int, float],
    depth_fraction: dict[int, float],
    base_pitch_deg: float,
) -> dict[int, tuple[float, float, float]]:
    center_angle = (angles[tooth_numbers[0]] + angles[tooth_numbers[-1]]) / 2
    extra_pitch = math.copysign(PITCH_DEPTH_SCALE_DEG, base_pitch_deg)
    return {
        tooth_number: (
            base_pitch_deg + extra_pitch * depth_fraction[tooth_number],
            angles[tooth_number] - center_angle,
            0.0,
        )
        for tooth_number in tooth_numbers
    }


_upper_offsets_2d, _upper_angles = _arc_offsets(UPPER_TEETH, _UPPER_ANGLE_RANGE, y_sign=+1)
_lower_offsets_2d, _lower_angles = _arc_offsets(LOWER_TEETH, _LOWER_ANGLE_RANGE, y_sign=-1)

_upper_depth_fraction = _depth_fraction(_upper_offsets_2d)
_lower_depth_fraction = _depth_fraction(_lower_offsets_2d)

TOOTH_OFFSETS_MM: dict[int, tuple[float, float]] = {
    **_upper_offsets_2d,
    **_lower_offsets_2d,
}

TOOTH_DEPTH_OFFSETS_MM: dict[int, float] = {
    **_depth_offsets(_upper_depth_fraction),
    **_depth_offsets(_lower_depth_fraction),
}

TOOTH_ROTATION_OFFSETS_DEG: dict[int, tuple[float, float, float]] = {
    **_rotation_offsets(UPPER_TEETH, _upper_angles, _upper_depth_fraction, UPPER_PITCH_OFFSET_DEG),
    **_rotation_offsets(LOWER_TEETH, _lower_angles, _lower_depth_fraction, LOWER_PITCH_OFFSET_DEG),
}