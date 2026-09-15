#session-based info
from dataclasses import dataclass
from core.enums import Phase


@dataclass
class ScanFlow:
    phase: Phase = Phase.IDLE
    target_reached: bool = False

    def mark_aligning(self) -> None:
        self.phase = Phase.ALIGNING
        self.target_reached = False

    def mark_target_reached(self) -> None:
        self.target_reached = True

    def mark_scanning(self) -> None:
        self.phase = Phase.SCANNING

    def mark_paused(self) -> None:
        self.phase = Phase.PAUSED

    def reset(self) -> None:
        self.phase = Phase.IDLE
        self.target_reached = False
  
