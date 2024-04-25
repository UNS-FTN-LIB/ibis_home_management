from enum import Enum

class SensorType(Enum):
    TEMPERATURE = 1
    HUMIDITY = 2
    MOTION = 3
    LIGHT = 4


class Sensor:
    def __init__(self, currentValue, type, name):
        self.name = name
        self.currentValue = currentValue
        self.type = type
