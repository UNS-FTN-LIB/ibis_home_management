import json
import  ConditionHandlerModel
import os
import MQTT_Broker
def HandleConditions(conditions):
    with open('ConditionsConfig.json', 'r') as f:
        conditionsConfigJson = f.read()

    conditionsConfig = json.loads(conditionsConfigJson)
    simulatorData = json.loads(conditions)
    clientscada = MQTT_Broker.connect_mqtt_scada()
    alertList = []
    for roomIdx,room in enumerate(simulatorData):
        model = ConditionHandlerModel.RoomConditionHandler()
        for sensor in room["sensors"]:
            MQTT_Broker.sendToScada(clientscada, sensor["topic"], sensor["currentValue"])
            # Access sensor data
            if("TEMPERATURE" in sensor["name"] ):
                if(sensor["currentValue"] < conditionsConfig["MIN_ACCEPTABLE_TEMP"] ):
                    model.heater_ON = 1
                    MQTT_Broker.sendToScada(clientscada, "IbisRoom"+str(roomIdx+1)+"Heater", 1)
                    MQTT_Broker.sendToScada(clientscada, "IbisRoom"+str(roomIdx+1)+"AC", 0)
                elif (sensor["currentValue"] > conditionsConfig["MAX_ACCEPTABLE_TEMP"]):
                    model.ac_ON = 1
                    MQTT_Broker.sendToScada(clientscada, "IbisRoom"+str(roomIdx+1)+"Heater", 0)
                    MQTT_Broker.sendToScada(clientscada, "IbisRoom"+str(roomIdx+1)+"AC", 1)
                else:
                    MQTT_Broker.sendToScada(clientscada, "IbisRoom"+str(roomIdx+1)+"Heater", 0)
                    MQTT_Broker.sendToScada(clientscada, "IbisRoom"+str(roomIdx+1)+"AC", 0)
            if ("HUMIDITY" in sensor["name"]):
                if (sensor["currentValue"] > conditionsConfig["MAX_ACCEPTABLE_HUMIDITY"]):
                    model.ventilation_ON = 1
                    MQTT_Broker.sendToScada(clientscada, "IbisRoom" + str(roomIdx+1) + "Vent", 1)
                else:
                    MQTT_Broker.sendToScada(clientscada, "IbisRoom" + str(roomIdx+1) + "Vent", 0)
            if ("MOTION" in sensor["name"]):
                if (sensor["currentValue"] == 1):
                    model.alarm_ON = 1
                    MQTT_Broker.sendToScada(clientscada, "IbisRoom" + str(roomIdx+1) + "Alarm", 1)
                else:
                    MQTT_Broker.sendToScada(clientscada, "IbisRoom" + str(roomIdx+1) + "Alarm", 0)
            if ("LIGHT" in sensor["name"]):
                if (sensor["currentValue"] < conditionsConfig["MIN_ACCEPTABLE_LIGHT"]):
                    model.light_ON = 1
                    MQTT_Broker.sendToScada(clientscada, "IbisRoom" + str(roomIdx+1) + "Blind", 0)
                    MQTT_Broker.sendToScada(clientscada, "IbisRoom" + str(roomIdx+1) + "Bulb", 1)
                elif (sensor["currentValue"] > conditionsConfig["MAX_ACCEPTABLE_LIGHT"]):
                    model.blind_ON = 1
                    MQTT_Broker.sendToScada(clientscada, "IbisRoom" + str(roomIdx+1) + "Blind", 1)
                    MQTT_Broker.sendToScada(clientscada, "IbisRoom" + str(roomIdx+1) + "Bulb", 0)
                else:
                    MQTT_Broker.sendToScada(clientscada, "IbisRoom" + str(roomIdx+1) + "Blind", 0)
                    MQTT_Broker.sendToScada(clientscada, "IbisRoom" + str(roomIdx+1) + "Bulb", 0)

        alertList.append(model.to_dict())

    file_path = "data.json"
    if os.path.exists(file_path):
        os.remove(file_path)

    with open(file_path, 'w') as json_file:
        json.dump(alertList, json_file, indent=4)

    jsonResponse = json.dumps(alertList, indent=4)
    return jsonResponse