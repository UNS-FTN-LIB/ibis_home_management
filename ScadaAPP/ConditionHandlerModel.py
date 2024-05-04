class RoomConditionHandler:
    def __init__(self, ac_ON = 0, ventilation_ON = 0 , alarm_ON = 0, heater_ON = 0, blind_ON = 0, light_ON = 0):
        self.ac_ON = ac_ON
        self.ventilation_ON = ventilation_ON
        self.alarm_ON = alarm_ON
        self.heater_ON = heater_ON
        self.blind_ON = blind_ON
        self.light_ON = light_ON

    def to_dict(self):
        return {
            "ac_ON": self.ac_ON,
            "ventilation_ON": self.ventilation_ON,
            "alarm_ON": self.alarm_ON,
            "heater_ON": self.heater_ON,
            "blind_ON": self.blind_ON,
            "light_ON": self.light_ON,
        }