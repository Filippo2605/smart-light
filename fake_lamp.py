import paho.mqtt.client as mqtt
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("CLOUD_AMQP_PASSWORD")
username = os.getenv("CLOUD_AMQP_USERNAME")

def on_message(client, userdata, msg):
    print("💡 LAMPADINA:", msg.payload.decode())

client = mqtt.Client()

# Use TLS for cloud connection
client.tls_set()  # enable encryption
client.username_pw_set(username=username, password=api_key)
client.connect("kebnekaise.lmq.cloudamqp.com", 8883)

client.subscribe("camera/luce")
client.on_message = on_message
client.loop_forever()
