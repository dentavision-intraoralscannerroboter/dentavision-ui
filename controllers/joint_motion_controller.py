from ui.motion_control_panel import build_motion_control_panel

ROTATION_AXES = ["rx", "ry", "rz"]


class MotionController:
    Z_STEP_MM = 1.0
    ROTATION_STEP_DEG = 5.0
    JOYSTICK_RANGE_MM = 10.0

    def __init__(self, motion_control_frame, on_move=None, on_z=None, on_rotate=None):
        self.on_move = on_move
        self.on_z = on_z
        self.on_rotate = on_rotate

        self._base_x = 0.0
        self._base_y = 0.0
        self._base_z = 0.0
        self._base_rotation = {axis: 0.0 for axis in ROTATION_AXES}

        self._z = 0.0
        self._rotation = {axis: 0.0 for axis in ROTATION_AXES}

        self.joystick = build_motion_control_panel(
            motion_control_frame,
            on_joystick_move=self._handle_move,
            on_z_step=self._nudge_z,
            on_rotate_step=self._rotate,
        )

    def set_baseline(self, x: float, y: float, z: float, rx: float, ry: float, rz: float) -> None:
        self._base_x, self._base_y, self._base_z = x, y, z
        self._base_rotation = {"rx": rx, "ry": ry, "rz": rz}
        self._z = 0.0
        self._rotation = {axis: 0.0 for axis in ROTATION_AXES}

    def _handle_move(self, x: float, y: float) -> None:
        actual_x = self._base_x + x * self.JOYSTICK_RANGE_MM
        actual_y = self._base_y + y * self.JOYSTICK_RANGE_MM
        print(f"Joystick: x={actual_x:.1f} mm, y={actual_y:.1f} mm")
        if self.on_move is not None:
            self.on_move(x, y)

    def _nudge_z(self, direction: int) -> None:
        self._z += direction * self.Z_STEP_MM
        actual_z = self._base_z + self._z
        print(f"Z: {actual_z:.1f} mm")
        if self.on_z is not None:
            self.on_z(actual_z)

    def _rotate(self, axis: str, direction: int) -> None:
        self._rotation[axis] += direction * self.ROTATION_STEP_DEG
        actual = self._base_rotation[axis] + self._rotation[axis]
        print(f"{axis.upper()}: {actual:.1f}°")
        if self.on_rotate is not None:
            self.on_rotate(axis, actual)