import SimulatorSrv.Client.WheatherForecastClient as wheatherForecast
import SimulatorSrv.Models.Device as device
import SimulatorSrv.Models.Room as room
import SimulatorSrv.Models.Sensor as sensor
from dataclasses import dataclass, asdict
import json
#TODO - IMPLEMENT DATA SIMULATION HERE

def generateRooms():
    rooms = []
    room1 = room.Room("Room1")
    room1.add_device(device.Device(state=False, name="AC-1", type=device.DeviceType.AC))
    room1.add_device(device.Device(state=False, name="VENTILATION1", type=device.DeviceType.VENTILATION))
    room1.add_device(device.Device(state=False, name="ALARM1", type=device.DeviceType.ALARM))
    room1.add_device(device.Device(state=False, name="HEATER1", type=device.DeviceType.HEATER))
    room1.add_sensor(sensor.Sensor(currentValue=20, type=sensor.SensorType.TEMPERATURE, name="TEMPERATURE1"))
    room1.add_sensor(sensor.Sensor(currentValue=20, type=sensor.SensorType.HUMIDITY, name="HUMIDITY1"))
    room1.add_sensor(sensor.Sensor(currentValue=20, type=sensor.SensorType.MOTION, name="MOTION1"))
    room1.add_sensor(sensor.Sensor(currentValue=20, type=sensor.SensorType.LIGHT, name="LIGHT1"))
    rooms.append(room1)
    room2 = room.Room("Room2")
    room2.add_device(device.Device(state=False, name="AC-2", type=device.DeviceType.AC))
    room2.add_device(device.Device(state=False, name="VENTILATION2", type=device.DeviceType.VENTILATION))
    room2.add_device(device.Device(state=False, name="ALARM2", type=device.DeviceType.ALARM))
    room2.add_device(device.Device(state=False, name="HEATER2", type=device.DeviceType.HEATER))
    room2.add_sensor(sensor.Sensor(currentValue=20, type=sensor.SensorType.TEMPERATURE, name="TEMPERATURE2"))
    room2.add_sensor(sensor.Sensor(currentValue=20, type=sensor.SensorType.HUMIDITY, name="HUMIDITY2"))
    room2.add_sensor(sensor.Sensor(currentValue=20, type=sensor.SensorType.MOTION, name="MOTION2"))
    room2.add_sensor(sensor.Sensor(currentValue=20, type=sensor.SensorType.LIGHT, name="LIGHT2"))
    rooms.append(room2)
    return rooms


def SimData(loadedWeather):
    rooms = generateRooms()  # Pretpostavka da generateRooms() vraća listu objekata soba
    for r in rooms:
        for s in r.sensors:
            s.currentValue = 10

    # Pretvaranje svake sobe u rečnik
    rooms_as_dicts = []
    for room in rooms:
        room_dict = {
            "devices": [],
            "sensors": []
        }
        for device in room.devices:
            device_dict = {
                "name": device.name,
                "state": device.state,
                "type": device.type.name,
            }
            room_dict["devices"].append(device_dict)
        for sensor in room.sensors:
            sensor_dict = {
                "name": sensor.name,
                "currentValue": sensor.currentValue,
                "type": sensor.type.name
            }
            room_dict["sensors"].append(sensor_dict)
        rooms_as_dicts.append(room_dict)

    room_json_str = json.dumps(rooms_as_dicts, indent=4)  # Pretvaranje liste rečnika u JSON format
    return room_json_str


