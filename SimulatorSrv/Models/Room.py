class Room:
    def __init__(self):
        self.devices = []
        self.sensors = []

    def add_device(self, device):
        self.devices.append(device)

    def add_sensor(self, sensor):
        self.sensors.append(sensor)