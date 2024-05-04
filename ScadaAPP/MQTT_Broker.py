import paho.mqtt.client as mqtt
import random
import ConditionHandler as conditionHandler
from paho.mqtt import client as mqtt_client


broker = 'localhost'
port = 1883
topic_simulator = "python/mqtt-simulator"
topic_client_response = "python/mqtt-clientResponse"
# Generate a Client ID with the subscribe prefix.
client_id = f'subscribe-{random.randint(0, 100)}'
# username = 'emqx'
# password = 'public'


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
        publish(client,alerts)
    client.subscribe(topic_simulator)
    client.on_message = on_message

    def publish(client, message):

        result = client.publish(topic_client_response, message)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{message}` to topic `{topic_client_response}`")

        else:
            print(f"Failed to send message to topic {topic_client_response}")


def mqttSubscribe():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()




