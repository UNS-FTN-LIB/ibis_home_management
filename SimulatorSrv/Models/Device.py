from enum import Enum
class DeviceType(Enum):
    AC = 1
    VENTILATION = 2
    ALARM = 3
    HEATER = 4

class Device:
    def __init__(self, state, name, type):
        self.name = name
        self.state = state
        self.type = type
