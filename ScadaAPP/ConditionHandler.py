import json
import  ConditionHandlerModel
def HandleConditions(conditions):
    with open('ConditionsConfig.json', 'r') as f:
        conditionsConfigJson = f.read()

    conditionsConfig = json.loads(conditionsConfigJson)
    simulatorData = json.loads(conditions)

    alertList = []
    for room in simulatorData:
        model = ConditionHandlerModel.RoomConditionHandler()
        for sensor in room["sensors"]:
            # Access sensor data
            if("TEMPERATURE" in sensor["name"] ):
                if(sensor["currentValue"] < conditionsConfig["MIN_ACCEPTABLE_TEMP"] ):
                    model.heater_ON = 1
                elif (sensor["currentValue"] > conditionsConfig["MAX_ACCEPTABLE_TEMP"]):
                    model.ac_ON = 1

            if ("HUMIDITY" in sensor["name"]):
                if (sensor["currentValue"] > conditionsConfig["MAX_ACCEPTABLE_HUMIDITY"]):
                    model.ventilation_ON = 1

            if ("MOTION" in sensor["name"]):
                if (sensor["currentValue"] == 1):
                    model.alarm_ON = 1

            if ("LIGHT" in sensor["name"]):
                if (sensor["currentValue"] < conditionsConfig["MIN_ACCEPTABLE_LIGHT"]):
                    model.light_ON = 1
                elif (sensor["currentValue"] > conditionsConfig["MAX_ACCEPTABLE_LIGHT"]):
                    model.blind_ON = 1

        alertList.append(model.to_dict())

    jsonResponse = json.dumps(alertList, indent=4)
    return jsonResponse