from core.teeth_data import TOOTH_OFFSETS_MM, TOOTH_DEPTH_OFFSETS_MM, TOOTH_ROTATION_OFFSETS_DEG, UPPER_TEETH

MM_PER_M = 1000.0
ROBOT_BASE_POSITION_M = (0.850, -0.000, 0.380)


def compute_tooth_target(tooth_number, head_position):
    dx, dy = TOOTH_OFFSETS_MM[tooth_number]
    dz = TOOTH_DEPTH_OFFSETS_MM[tooth_number]
    drx, dry, drz = TOOTH_ROTATION_OFFSETS_DEG[tooth_number]

    x_mm = head_position.x + dx
    y_mm = head_position.y + dy
    z_mm = head_position.z + dz

    rx = head_position.rx + drx
    ry = head_position.ry + dry
    rz = head_position.rz + drz

    x = x_mm / MM_PER_M
    y = y_mm / MM_PER_M
    z = z_mm / MM_PER_M

    return (x, y, z, rx, ry, rz)


def compute_tooth_target_robot_frame(tooth_number, head_position):
    x, y, z, rx, ry, rz = compute_tooth_target(tooth_number, head_position)

    base_x, base_y, base_z = ROBOT_BASE_POSITION_M
    return (base_x + x, base_y + y, base_z + z, rx, ry, rz)

# helper method to get the command for the demo from terminal
def get_demo_command(tooth_number, head_position) -> str:
    side = "upper" if tooth_number in UPPER_TEETH else "lower"
    x, y, z, rx, ry, rz = compute_tooth_target_robot_frame(tooth_number, head_position)
    return (
        f"jaw {tooth_number} {side}\n"
        f"m {x:.4f} {y:.4f} {z:.4f} {rx:.1f} {ry:.1f} {rz:.1f}"
    )