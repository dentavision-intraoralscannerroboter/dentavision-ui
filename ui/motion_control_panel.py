from __future__ import annotations

import math

from PySide6.QtCore import Qt, QPointF
from PySide6.QtGui import QPainter, QPen, QBrush, QColor
from PySide6.QtWidgets import QLabel, QPushButton, QWidget

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
JOYSTICK_DIAMETER = 90
TOP_OFFSET = 15


class JoystickWidget(QWidget):
    KNOB_RADIUS = 15
    TRACK_COLOR = "#118983"

    def __init__(self, diameter: int = 120, on_move=None, parent=None):
        super().__init__(parent)
        self.diameter = diameter
        self.on_move = on_move
        self._knob_offset = QPointF(0, 0)
        self._dragging = False

        self.setFixedSize(diameter, diameter)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setStyleSheet("background: transparent;")

    def _center(self) -> QPointF:
        return QPointF(self.width() / 2, self.height() / 2)

    def _max_offset(self) -> float:
        return self.diameter / 2 - self.KNOB_RADIUS

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        track_rect = self.rect().adjusted(2, 2, -2, -2)
        painter.setPen(QPen(QColor(self.TRACK_COLOR), 2))
        painter.setBrush(Qt.NoBrush)
        painter.drawEllipse(track_rect)

        knob_center = self._center() + self._knob_offset
        painter.setPen(Qt.NoPen)
        painter.setBrush(QBrush(QColor(self.TRACK_COLOR)))
        painter.drawEllipse(knob_center, self.KNOB_RADIUS, self.KNOB_RADIUS)

    def _update_from_mouse(self, pos: QPointF) -> None:
        center = self._center()
        offset = QPointF(pos.x() - center.x(), pos.y() - center.y())

        max_offset = self._max_offset()
        distance = math.hypot(offset.x(), offset.y())
        if distance > max_offset:
            scale = max_offset / distance
            offset = QPointF(offset.x() * scale, offset.y() * scale)

        self._knob_offset = offset
        self.update()

        if self.on_move is not None:
            x = offset.x() / max_offset
            y = -offset.y() / max_offset
            self.on_move(x, y)

    def mousePressEvent(self, event):
        self._dragging = True
        self._update_from_mouse(event.position())

    def mouseMoveEvent(self, event):
        if self._dragging:
            self._update_from_mouse(event.position())

    def mouseReleaseEvent(self, event):
        self._dragging = False
        self._knob_offset = QPointF(0, 0)
        self.update()
        if self.on_move is not None:
            self.on_move(0.0, 0.0)


def _styled_button(parent, text, x, y, w, h, on_click):
    btn = QPushButton(text, parent)
    btn.setGeometry(x, y, w, h)
    btn.setStyleSheet(BUTTON_STYLE)
    btn.clicked.connect(on_click)
    btn.show()
    return btn


def _build_z_control(parent, on_z_step):
    _styled_button(parent, "▲", 112, 55 + TOP_OFFSET, 34, 26, lambda: on_z_step(+1))
    z_label = QLabel("Z", parent)
    z_label.setGeometry(112, 83 + TOP_OFFSET, 34, 16)
    z_label.setAlignment(Qt.AlignCenter)
    z_label.setStyleSheet(LABEL_STYLE)
    z_label.show()
    _styled_button(parent, "▼", 112, 101 + TOP_OFFSET, 34, 26, lambda: on_z_step(-1))


def _build_rotation_row(parent, axis, y, on_rotate_step):
    label = QLabel(axis.upper(), parent)
    label.setGeometry(158, y, 26, 22)
    label.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
    label.setStyleSheet(LABEL_STYLE)
    label.show()
    _styled_button(parent, "−", 186, y, 24, 22, lambda: on_rotate_step(axis, -1))
    _styled_button(parent, "+", 214, y, 24, 22, lambda: on_rotate_step(axis, +1))


def build_motion_control_panel(parent_frame, on_joystick_move, on_z_step, on_rotate_step):
    joystick = JoystickWidget(
        diameter=JOYSTICK_DIAMETER,
        on_move=on_joystick_move,
        parent=parent_frame,
    )
    joystick.move(10, 50 + TOP_OFFSET)
    joystick.show()

    _build_z_control(parent_frame, on_z_step)
    for i, axis in enumerate(ROTATION_AXES):
        _build_rotation_row(parent_frame, axis, y=52 + TOP_OFFSET + i * 26, on_rotate_step=on_rotate_step)

    return joystick