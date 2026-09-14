from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QPushButton

from ui.joystick_widget import JoystickWidget

BUTTON_STYLE = """
    QPushButton {
        border: 2px solid #118983;
        border-radius: 6px;
        background-color: white;
        color: #118983;
        font-weight: bold;
        font-size: 11px;
    }
    QPushButton:hover {
        background-color: #e8f5f0;
    }
"""
LABEL_STYLE = "color: #768599; font-weight: 600; font-size: 11px;"

ROTATION_AXES = ["rx", "ry", "rz"]


class MotionController:
    JOYSTICK_DIAMETER = 90
    Z_STEP_MM = 1.0
    ROTATION_STEP_DEG = 5.0
    TOP_OFFSET = 15
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

        self.joystick = JoystickWidget(
            diameter=self.JOYSTICK_DIAMETER,
            on_move=self._handle_move,
            parent=motion_control_frame,
        )
        self.joystick.move(10, 50 + self.TOP_OFFSET)
        self.joystick.show()

        self._build_z_control(motion_control_frame)
        for i, axis in enumerate(ROTATION_AXES):
            self._build_rotation_row(motion_control_frame, axis, y=52 + self.TOP_OFFSET + i * 26)

    def set_baseline(self, x: float, y: float, z: float, rx: float, ry: float, rz: float) -> None:
        self._base_x, self._base_y, self._base_z = x, y, z
        self._base_rotation = {"rx": rx, "ry": ry, "rz": rz}
        self._z = 0.0
        self._rotation = {axis: 0.0 for axis in ROTATION_AXES}

    def _button(self, parent, text, x, y, w, h, on_click):
        btn = QPushButton(text, parent)
        btn.setGeometry(x, y, w, h)
        btn.setStyleSheet(BUTTON_STYLE)
        btn.clicked.connect(on_click)
        btn.show()
        return btn

    def _build_z_control(self, parent):
        self._button(parent, "▲", 112, 55 + self.TOP_OFFSET, 34, 26, lambda: self._nudge_z(+1))
        z_label = QLabel("Z", parent)
        z_label.setGeometry(112, 83 + self.TOP_OFFSET, 34, 16)
        z_label.setAlignment(Qt.AlignCenter)
        z_label.setStyleSheet(LABEL_STYLE)
        z_label.show()
        self._button(parent, "▼", 112, 101 + self.TOP_OFFSET, 34, 26, lambda: self._nudge_z(-1))

    def _build_rotation_row(self, parent, axis, y):
        label = QLabel(axis.upper(), parent)
        label.setGeometry(158, y, 26, 22)
        label.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        label.setStyleSheet(LABEL_STYLE)
        label.show()
        self._button(parent, "−", 186, y, 24, 22, lambda: self._rotate(axis, -1))
        self._button(parent, "+", 214, y, 24, 22, lambda: self._rotate(axis, +1))

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