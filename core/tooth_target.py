from core.models import HeadPosition
from core.teeth_data import TOOTH_OFFSETS_MM, TOOTH_DEPTH_OFFSETS_MM, TOOTH_ROTATION_OFFSETS_DEG


def compute_tooth_target(tooth_number, head_position):
    dx, dy = TOOTH_OFFSETS_MM[tooth_number]
    dz = TOOTH_DEPTH_OFFSETS_MM[tooth_number]
    drx, dry, drz = TOOTH_ROTATION_OFFSETS_DEG[tooth_number]

    x = head_position.x + dx
    y = head_position.y + dy
    z = head_position.z + dz

    rx = head_position.rx + drx
    ry = head_position.ry + dry
    rz = head_position.rz + drz

    return (x, y, z, rx, ry, rz)