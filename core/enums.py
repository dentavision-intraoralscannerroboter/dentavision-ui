from enum import Enum,auto 

class Phase(Enum):
    IDLE = auto()
    ALIGNING = auto()
    SCANNING = auto()
    PAUSED = auto()