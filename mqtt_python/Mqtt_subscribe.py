import paho.mqtt.client as mqtt
import json

broker_url = "broker.emqx.io"
broker_port = 1883

client = mqtt.Client()

client.connect(broker_url,broker_port)

def on_message(client,userdata,msg):
    jsonString = msg.payload.decode("utf-8")
    jsonData = json.loads(jsonString)
    print("{}-{}".format(jsonData["name"],jsonData["email"]))
    

client.on_message = on_message
client.subscribe("topic_name",qos=0)
client.loop_forever()