
import random
import ConditionHandler as conditionHandler
from paho.mqtt import client as mqtt_client


broker = 'localhost'
port = 1883
topic_simulator = "python/mqtt-simulator"
topic_client_response = "python/mqtt-clientResponse"
client_id = f'subscribe-{random.randint(0, 100)}'

client_id_scada = f'publish-{random.randint(0, 1000)}'
broker_scada = 'broker.hivemq.com'
port_scada = 1883

def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        #TODO - READ NEW DATA AND CHANGE SCADA STATE
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        alerts = conditionHandler.HandleConditions(msg.payload.decode())
        print(f"Alerts ready: `{alerts}`")

    client.subscribe(topic_simulator)
    client.on_message = on_message

def mqttSubscribe():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()

def connect_mqtt_scada():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id_scada)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker_scada, port_scada)
    return client

def sendToScada(client, topic, value):
    result = client.publish(topic, value)
    # result: [0, 1]
    status = result[0]
    if status == 0:
        print(f"Send `{value}` to topic `{topic}`")
    else:
        print(f"Failed to send message to topic {value}")