from core.models import HeadPosition, Tooth
from core.tooth_target import compute_tooth_target


class ToothTargetController:

    def __init__(self, ui, head_position: HeadPosition):
        self.ui = ui
        self.head_position = head_position

    def show_target_for(self, tooth: Tooth) -> tuple[float, float, float, float, float, float]:
        x, y, z, rx, ry, rz = compute_tooth_target(tooth.number, self.head_position)
        self.ui.labelX.setText(f"{x:.4f} m")
        self.ui.labelY.setText(f"{y:.4f} m")
        self.ui.labelZ.setText(f"{z:.4f} m")
        self.show_orientation(rx, ry, rz)
        return (x, y, z, rx, ry, rz)

    def show_orientation(self, rx: float, ry: float, rz: float) -> None:
        self.ui.labelX_2.setText(f"{rx:.1f}°")
        self.ui.labelY_2.setText(f"{ry:.1f}°")
        self.ui.labelZ_2.setText(f"{rz:.1f}°")

    def clear(self) -> None:
        self.ui.labelX.setText("-")
        self.ui.labelY.setText("-")
        self.ui.labelZ.setText("-")
        self.ui.labelX_2.setText("-")
        self.ui.labelY_2.setText("-")
        self.ui.labelZ_2.setText("-")