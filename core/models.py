from dataclasses import dataclass, field


@dataclass
class Tooth:
    number: int
    name: str
    x: float
    y: float
    z: float

    def move_x(self, amount):
        self.x += amount

    def move_y(self, amount):
        self.y += amount

    def move_z(self, amount):
        self.z += amount

    def position(self) -> tuple[float, float, float]:
        return (self.x, self.y, self.z)


@dataclass
class Joint:
    # Single robot joint (J1-J6) in joint-space.
    # Not wired, not used. Maybe used in future implementations, when the system is fully connected.
    # MotionController's Cartesian delta into per-joint angles.
    name: str
    angle: float
    min_angle: float = -180.0
    max_angle: float = 180.0

    def set_angle(self, value: float):
        self.angle = max(self.min_angle, min(self.max_angle, value))

    def increment(self, step: float):
        self.set_angle(self.angle + step)

    def decrement(self, step: float):
        self.set_angle(self.angle - step)


@dataclass
class RobotArm:
    # not wired, not used. Maybe used in future implementations. 
    # Joint-space snapshot of the whole arm.
    # Consumer: a future IK function (core/kinematics.py) that turns
    # a Cartesian target pose into joint angles before sending to the robot.
    joints: list[Joint] = field(default_factory=lambda: [
        Joint(name=f"J{i}", angle=0.0) for i in range(1, 7)
    ])

    def get_joint(self, name: str) -> Joint:
        for j in self.joints:
            if j.name == name:
                return j
        raise ValueError(f"Joint not found: {name}")

@dataclass
class HeadPosition:
    detected: bool = False
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0
    rx: float = 0.0
    ry: float = 0.0
    rz: float = 0.0