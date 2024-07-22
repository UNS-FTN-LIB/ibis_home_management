import random
import time
from paho.mqtt import client as mqtt_client

broker = 'localhost'
port = 1883
topic_simulator = "python/mqtt-simulator"
topic_client_response = "python/mqtt-clientResponse"
# Generate a Client ID with the publish prefix.
client_id = f'publish-{random.randint(0, 1000)}'

def connect_mqtt():
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


def publish(client,message):

        result = client.publish(topic_simulator, message)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{message}` to topic `{topic_simulator}`")
        else:
            print(f"Failed to send message to topic {topic_simulator}")


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        #TODO - READ NEW DATA AND CHANGE SCADA STATE
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        client.disconnect()
    client.subscribe(topic_client_response)
    client.on_message = on_message



def startConnection():
    return connect_mqtt()

def sendData(client,message):
    publish(client)


