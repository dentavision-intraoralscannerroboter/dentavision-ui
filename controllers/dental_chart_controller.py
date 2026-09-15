from core.models import Tooth
from core.teeth_data import UPPER_TEETH, LOWER_TEETH, TOOTH_NAMES
from ui.dental_chart import build_dental_chart, set_normal_style, set_selected_style


class DentalChartController:

    def __init__(self, mouth_frame, on_tooth_selected=None, can_select=None):
        self.mouth_frame = mouth_frame
        self.on_tooth_selected = on_tooth_selected
        self.can_select = can_select
        self.teeth = {
            number: Tooth(number=number, name=name, x=0.0, y=0.0, z=0.0)
            for number, name in TOOTH_NAMES.items()
        }
        self.selected_tooth = None

        self.tooth_buttons = build_dental_chart(
            mouth_frame, UPPER_TEETH, LOWER_TEETH, on_click=self._handle_click
        )

    def _handle_click(self, tooth_number):
        if self.can_select is not None and not self.can_select():
            return

        if self.selected_tooth is not None:
            prev_btn = self.tooth_buttons[self.selected_tooth.number]
            set_normal_style(prev_btn)

        tooth = self.teeth[tooth_number]
        self.selected_tooth = tooth
        selected_btn = self.tooth_buttons[tooth_number]
        set_selected_style(selected_btn)

        if self.on_tooth_selected:
            self.on_tooth_selected(tooth)

    def clear_selection(self) -> None:
        if self.selected_tooth is not None:
            set_normal_style(self.tooth_buttons[self.selected_tooth.number])
            self.selected_tooth = None