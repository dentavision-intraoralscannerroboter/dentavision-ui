from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel

STABILIZATION_ERROR_STYLE = """
    QLabel {
        background-color: #C83C3C;
        color: white;
        font-weight: bold;
        font-size: 13px;
        border-radius: 8px;
        padding: 6px 14px;
    }
"""


def build_stabilization_error_label(center_panel) -> QLabel:
    label = QLabel("STABILIZATION ERROR", center_panel)
    label.setAlignment(Qt.AlignCenter)
    label.setStyleSheet(STABILIZATION_ERROR_STYLE)
    label.adjustSize()
    label.move((center_panel.width() - label.width()) // 2, 10)
    label.hide()
    return label