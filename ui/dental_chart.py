from __future__ import annotations

import math

from PySide6.QtWidgets import QPushButton

NORMAL_STYLE = """
    QPushButton {
        border: 2px solid #118983;
        border-radius: 17px;
        background-color: white;
        color: #118983;
        font-weight: bold;
    }
    QPushButton:hover {
        background-color: #e8f5f0;
    }
"""

SELECTED_STYLE = """
    QPushButton {
        border: 2px solid #118983;
        border-radius: 17px;
        background-color: #118983;
        color: white;
        font-weight: bold;
    }
"""


def set_normal_style(button: QPushButton) -> None:
    button.setStyleSheet(NORMAL_STYLE)


def set_selected_style(button: QPushButton) -> None:
    button.setStyleSheet(SELECTED_STYLE)


def _place_teeth_on_arc(mouth_frame, tooth_numbers, cx, cy, rx, ry, size,
                         start_angle, end_angle, on_click):
    buttons = {}
    count = len(tooth_numbers)
    for i, tooth_num in enumerate(tooth_numbers):
        angle_deg = start_angle + (end_angle - start_angle) * i / (count - 1)
        angle_rad = math.radians(angle_deg)

        x = cx + rx * math.cos(angle_rad) - size / 2
        y = cy + ry * math.sin(angle_rad) - size / 2

        button = QPushButton(str(tooth_num), mouth_frame)
        button.setGeometry(int(x), int(y), size, size)
        set_normal_style(button)
        button.clicked.connect(lambda checked, n=tooth_num: on_click(n))
        button.show()

        buttons[tooth_num] = button
    return buttons


def build_dental_chart(mouth_frame, upper_teeth, lower_teeth, on_click):

    width = mouth_frame.width()
    height = mouth_frame.height()
    center_x = width / 2
    center_y = height / 2
    radius_x = width / 2 - 30
    radius_y = height / 2 - 30
    button_size = 34

    buttons = {}
    buttons.update(_place_teeth_on_arc(
        mouth_frame, upper_teeth, center_x, center_y,
        radius_x, radius_y, button_size,
        start_angle=195, end_angle=345, on_click=on_click,
    ))
    buttons.update(_place_teeth_on_arc(
        mouth_frame, lower_teeth, center_x, center_y,
        radius_x, radius_y, button_size,
        start_angle=165, end_angle=15, on_click=on_click,
    ))
    return buttons