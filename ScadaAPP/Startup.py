import MQTT_Broker as mqtt
from flask import Flask, request, jsonify
import threading,json
import sys
app = Flask(__name__)
@app.route('/client-response')
def hello():
    with open("data.json", 'r') as json_file:
        data = json.load(json_file)
    return jsonify({"Alerts": data})

def start_flask():
    app.run(debug=True, port=5000, use_reloader=False)



if __name__ == '__main__':
    t1 = threading.Thread(target = start_flask)
    t1.daemon = True
    t1.start()
    mqtt.mqttSubscribe()

