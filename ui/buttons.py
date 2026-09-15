START_BUTTON_STYLE = """
    QPushButton {
        background-color: #0E7772;
        color: white;
        border: none;
        border-radius: 10px;
        padding: 6px 20px;
        font-weight: bold;
    }
    QPushButton:hover {
        background-color: #129B93;
    }
    QPushButton:pressed {
        background-color: #0B5F5B;
    }
    QPushButton:disabled {
        background-color: #A9C9C7;
        color: #F0F0F0;
    }
"""


def style_start_button(button) -> None:
    button.setStyleSheet(START_BUTTON_STYLE)


START_TEXT = "Start"
SCAN_TEXT = "Scan"
PAUSE_TEXT = "Pause"


def set_start_text(button) -> None:
    button.setText(START_TEXT)


def set_scan_text(button) -> None:
    button.setText(SCAN_TEXT)


def set_pause_text(button) -> None:
    button.setText(PAUSE_TEXT)