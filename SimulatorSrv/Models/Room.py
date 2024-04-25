class Room:
    def __init__(self, name):
        self.name = name
        self.devices = []
        self.sensors = []

    def add_device(self, device):
        self.devices.append(device)

    def add_sensor(self, sensor):
        self.sensors.append(sensor)

    def update_device_value(self, device_name, new_value):
        for device in self.devices:
            if device.name == device_name:
                device.setValue = new_value
                break  # Prekidamo petlju ako je uređaj pronađen

    def update_sensor_value(self, sensor_type, new_value):
        for sensor in self.sensors:
            if sensor.sensor_type == sensor_type:
                sensor.currentValue = new_value
                break  # Prekidamo petlju ako je senzor pronađen