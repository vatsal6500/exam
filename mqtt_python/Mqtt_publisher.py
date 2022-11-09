import paho.mqtt.client as mqtt
import json

broker_url = "broker.emqx.io"
broker_port = 1883

client = mqtt.Client()


client.connect(broker_url,broker_port)

def on_publish(client,userdata,mid):
    print("Message has been published")


# client.on_publish = on_publish

empData = {"name":"abc","email":"abc@gmail.com"}

jsonStringEmpData = json.dumps(empData)


client.publish(topic="topic_name",payload=jsonStringEmpData,qos=0,retain=False)
