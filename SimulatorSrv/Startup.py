
import MQTT_Broker as mqttPublisher
import threading
import time
import Services.SimdataService as simDataService

def MQTTMessagingLoop():
    while(1):
        data = simDataService.SimData()
        mqttPublisher.publish(publisher,data)
        time.sleep(5)




if __name__ == '__main__':
    publisher = mqttPublisher.startConnection()
    #start sending simulated data to queue on every 5 seconds
    t1 = threading.Thread(target=MQTTMessagingLoop())
    t1.start()

