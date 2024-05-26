import SimulatorSrv.Client.WheatherForecastClient as wheatherForecast
import SimulatorSrv.Models.Device as device
import SimulatorSrv.Models.Room as room
import SimulatorSrv.Models.Sensor as sensor
from dataclasses import dataclass, asdict
import json, requests,os
import random
import SimulatorSrv.MQTT_Broker as MQTT_Broker
from datetime import datetime

#TODO - IMPLEMENT DATA SIMULATION HERE


def generateRooms():
    rooms = []
    room1 = room.Room("Room1")
    room1.add_device(device.Device(state=False, name="AC-1", type=device.DeviceType.AC, topic="IbisRoom1AC"))
    room1.add_device(device.Device(state=False, name="VENTILATION1", type=device.DeviceType.VENTILATION, topic="IbisRoom1Vent"))
    room1.add_device(device.Device(state=False, name="ALARM1", type=device.DeviceType.ALARM, topic="IbisRoom1Alarm"))
    room1.add_device(device.Device(state=False, name="HEATER1", type=device.DeviceType.HEATER, topic="IbisRoom1Heater"))
    room1.add_device(device.Device(state=False, name="BLIND1", type=device.DeviceType.BLIND, topic="IbisRoom1Blind"))
    room1.add_device(device.Device(state=False, name="LIGHT1", type=device.DeviceType.LIGHT, topic="IbisRoom1Light"))
    room1.add_sensor(sensor.Sensor(currentValue=20, type=sensor.SensorType.TEMPERATURE, name="TEMPERATURE1", topic="IbisRoom1Temp"))
    room1.add_sensor(sensor.Sensor(currentValue=20, type=sensor.SensorType.HUMIDITY, name="HUMIDITY1", topic="IbisRoom1Huminity"))
    room1.add_sensor(sensor.Sensor(currentValue=20, type=sensor.SensorType.MOTION, name="MOTION1", topic="IbisRoom1Motion"))
    room1.add_sensor(sensor.Sensor(currentValue=20, type=sensor.SensorType.LIGHT, name="LIGHT1", topic="IbisRoom1Light"))
    rooms.append(room1)
    room2 = room.Room("Room2")
    room2.add_device(device.Device(state=False, name="AC-2", type=device.DeviceType.AC, topic="IbisRoom2AC"))
    room2.add_device(device.Device(state=False, name="VENTILATION2", type=device.DeviceType.VENTILATION, topic="IbisRoom2Vent"))
    room2.add_device(device.Device(state=False, name="ALARM2", type=device.DeviceType.ALARM, topic="IbisRoom2Alarm"))
    room2.add_device(device.Device(state=False, name="HEATER2", type=device.DeviceType.HEATER, topic="IbisRoom2Heater"))
    room2.add_device(device.Device(state=False, name="BLIND2", type=device.DeviceType.BLIND, topic="IbisRoom2Blind"))
    room2.add_device(device.Device(state=False, name="LIGHT2", type=device.DeviceType.LIGHT, topic="IbisRoom2Light"))
    room2.add_sensor(sensor.Sensor(currentValue=20, type=sensor.SensorType.TEMPERATURE, name="TEMPERATURE2", topic="IbisRoom2Temp"))
    room2.add_sensor(sensor.Sensor(currentValue=20, type=sensor.SensorType.HUMIDITY, name="HUMIDITY2", topic="IbisRoom2Huminity"))
    room2.add_sensor(sensor.Sensor(currentValue=20, type=sensor.SensorType.MOTION, name="MOTION2", topic="IbisRoom2Motion"))
    room2.add_sensor(sensor.Sensor(currentValue=20, type=sensor.SensorType.LIGHT, name="LIGHT2", topic="IbisRoom2Light"))
    rooms.append(room2)
    room3 = room.Room("Room3")
    room3.add_device(device.Device(state=False, name="AC-3", type=device.DeviceType.AC, topic="IbisRoom3AC"))
    room3.add_device(device.Device(state=False, name="VENTILATION3", type=device.DeviceType.VENTILATION, topic="IbisRoom3Vent"))
    room3.add_device(device.Device(state=False, name="ALARM3", type=device.DeviceType.ALARM, topic="IbisRoom3Alarm"))
    room3.add_device(device.Device(state=False, name="HEATER3", type=device.DeviceType.HEATER, topic="IbisRoom3Heater"))
    room3.add_device(device.Device(state=False, name="BLIND3", type=device.DeviceType.BLIND, topic="IbisRoom3Blind"))
    room3.add_device(device.Device(state=False, name="LIGHT3", type=device.DeviceType.LIGHT, topic="IbisRoom3Light"))
    room3.add_sensor(sensor.Sensor(currentValue=20, type=sensor.SensorType.TEMPERATURE, name="TEMPERATURE3", topic="IbisRoom3Temp"))
    room3.add_sensor(sensor.Sensor(currentValue=20, type=sensor.SensorType.HUMIDITY, name="HUMIDITY3", topic="IbisRoom3Huminity"))
    room3.add_sensor(sensor.Sensor(currentValue=20, type=sensor.SensorType.MOTION, name="MOTION3", topic="IbisRoom3Motion"))
    room3.add_sensor(sensor.Sensor(currentValue=20, type=sensor.SensorType.LIGHT, name="LIGHT3", topic="IbisRoom3Light"))
    rooms.append(room3)
    room4 = room.Room("Room4")
    room4.add_device(device.Device(state=False, name="AC-4", type=device.DeviceType.AC, topic="IbisRoom4AC"))
    room4.add_device(device.Device(state=False, name="VENTILATION4", type=device.DeviceType.VENTILATION, topic="IbisRoom4Vent"))
    room4.add_device(device.Device(state=False, name="ALARM4", type=device.DeviceType.ALARM, topic="IbisRoom4Alarm"))
    room4.add_device(device.Device(state=False, name="HEATER4", type=device.DeviceType.HEATER, topic="IbisRoom4Heater"))
    room4.add_device(device.Device(state=False, name="BLIND4", type=device.DeviceType.BLIND, topic="IbisRoom4Blind"))
    room4.add_device(device.Device(state=False, name="LIGHT4", type=device.DeviceType.LIGHT, topic="IbisRoom4Light"))
    room4.add_sensor(sensor.Sensor(currentValue=20, type=sensor.SensorType.TEMPERATURE, name="TEMPERATURE4", topic="IbisRoom4Temp"))
    room4.add_sensor(sensor.Sensor(currentValue=20, type=sensor.SensorType.HUMIDITY, name="HUMIDITY4", topic="IbisRoom4Huminity"))
    room4.add_sensor(sensor.Sensor(currentValue=20, type=sensor.SensorType.MOTION, name="MOTION4", topic="IbisRoom4Motion"))
    room4.add_sensor(sensor.Sensor(currentValue=20, type=sensor.SensorType.LIGHT, name="LIGHT4", topic="IbisRoom4Light"))
    rooms.append(room4)
    return rooms

def generateDefaultValue(weather, s, devs):  #TODO OVA FUNKCIJA SE KORISTI KAD SIMULATOR PRVI PUT SALJE VREDNOSTI
    if s.type == sensor.SensorType.TEMPERATURE:
        temp = weather.value["forecast"]["forecastday"][0]["day"]["avgtemp_c"]  # trenutni vremensku uslovi danas
        # TO DO: Pronadji device koji odgovara ovom senzoru
        # proveri da li je device upaljen ili ugasen, i onda smanji ili povecaj vrednot u odnosu na to.
        # isto vazi za sve ostale
        return temp
    elif s.type == sensor.SensorType.HUMIDITY:
        return random.randint(1, 100)
    elif s.type == sensor.SensorType.MOTION:
        return random.randint(0, 1)
    elif s.type == sensor.SensorType.LIGHT:
        return random.randint(1, 100)


def generateValue(activeConditions, clientResponseAlerts, s, devs, sensor_index, room_index,loadedWheather):
    if s.type == sensor.SensorType.TEMPERATURE:
        if(clientResponseAlerts["Alerts"][room_index]["heater_ON"] == 1):
            oldTempValue = activeConditions[room_index]["sensors"][0]["currentValue"]
            newTempValue = oldTempValue + 0.3 if oldTempValue < 40 else oldTempValue
            return newTempValue;
        elif(clientResponseAlerts["Alerts"][room_index]["ac_ON"] == 1):
            oldTempValue = activeConditions[room_index]["sensors"][0]["currentValue"]
            newTempValue = oldTempValue - 0.3 if oldTempValue > 12 else oldTempValue
            return newTempValue;
        else:
            outsideTemp = loadedWheather.value["forecast"]["forecastday"][0]["day"]["avgtemp_c"]
            oldTempValue = activeConditions[room_index]["sensors"][0]["currentValue"]
            return oldTempValue + (outsideTemp - oldTempValue) * 0.005



    elif s.type == sensor.SensorType.HUMIDITY:
        current_value = activeConditions[room_index]["sensors"][1]["currentValue"]
        if clientResponseAlerts["Alerts"][room_index]["ventilation_ON"] == 1:
            return current_value - 0.3 if current_value - 0.3 > 0 else current_value
        else:
            randChange = random.randint(-2,2)
            return current_value + randChange if current_value + randChange >0 and current_value + randChange <= 100 else current_value


    elif s.type == sensor.SensorType.MOTION:
        random_number = random.randint(1, 100)
        if(clientResponseAlerts["Alerts"][room_index]["alarm_ON"] == 1):
            if(random_number <=50):
                return 0
            else:
                return 1
        else:
            if(random_number <=5):
                return 1
            else:
                return 0



    elif s.type == sensor.SensorType.LIGHT:
        current_value = activeConditions[room_index]["sensors"][3]["currentValue"]
        if clientResponseAlerts["Alerts"][room_index]["light_ON"] == 1:
            return 80

        elif clientResponseAlerts["Alerts"][room_index]["blind_ON"] == 1:
            return current_value - current_value * 0.4

        else:
            return random.randint(1, 100)

    #TODO UBACITI LOGIKU IZMENE VREDNOSTI SIMULATORA VREMNOM U ODNOSU NA UPALJENE UREDJAJE I PRETHODNE VREDNOSTI





def SimData(loadedWeather):
    ReciveAlertsFromCLient()
    rooms = generateRooms()  # Pretpostavka da generateRooms() vraća listu objekata soba
    if (os.path.exists("../activeConditions.json") == False):  #U OVAJ FAJL SE UPISUJE STA JE SIMULATOR PRETHODNO POSLAO
        for r in rooms:
            for s in r.sensors:
                s.currentValue = generateDefaultValue(loadedWeather, s, r.devices)
    else:
        with open("../activeConditions.json", 'r') as json_file:
            activeConditions = json.load(json_file)
        with open("../clientResponseAlerts.json", 'r') as json_file:
            clientResponseAlerts = json.load(json_file)
        for room_index,r in enumerate(rooms):
            for sensor_index,s in enumerate(r.sensors):
                s.currentValue = generateValue(activeConditions,clientResponseAlerts, s, r.devices, sensor_index, room_index,loadedWeather)
                #TODO KORISTIMO PRETHODNE VREDNOSTI SIMULATORA I POVRATNE VREDNOSTI SCADE DA OSMISLIMO NOVE VREDNOSTI

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
                "topic": device.topic,
            }
            room_dict["devices"].append(device_dict)
        for sensor in room.sensors:
            sensor_dict = {
                "name": sensor.name,
                "currentValue": sensor.currentValue,
                "type": sensor.type.name,
                "topic": sensor.topic
            }
            room_dict["sensors"].append(sensor_dict)
        rooms_as_dicts.append(room_dict)

    with open("../activeConditions.json", 'w') as json_file:
        json.dump(rooms_as_dicts, json_file, indent=4)   #TODO SVAKI PUT UPISEMO ONO STO JE SIMULATOR POSLAO
    room_json_str = json.dumps(rooms_as_dicts, indent=4)  # Pretvaranje liste rečnika u JSON format
    return room_json_str


def ReciveAlertsFromCLient():

    response = requests.get("http://localhost:5000/client-response")
    if response.status_code == 200:
        with open("../clientResponseAlerts.json", 'w') as json_file:
            json.dump(response.json(), json_file, indent=4)
            #TODO STOROVALI SMO POVRATNU VREDNOST SCADE I TE PODATKE KORISTIMO PRILIKOM GENERISANJA NOVOH VREDNOSTI
