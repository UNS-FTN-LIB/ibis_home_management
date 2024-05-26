from enum import Enum
class DeviceType(Enum):
    AC = 1
    VENTILATION = 2
    ALARM = 3
    HEATER = 4
    BLIND = 5
    LIGHT = 6

class Device:
    def __init__(self, state, name, type, topic):
        self.name = name
        self.state = state
        self.type = type
        self.topic = topic
