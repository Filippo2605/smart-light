from fastapi import FastAPI
import paho.mqtt.publish as publish
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("CLOUD_AMQP_PASSWORD")

app = FastAPI()
TOPIC = "casa/lampada"

@app.post("/on")
def accendi():
    publish.single(
        TOPIC,
        "ON",
        hostname="kebnekaise.lmq.cloudamqp.com",
        port=8883,
        tls={'ca_certs': None},  # optional for self-signed certificates
        auth={'username': "qjcmdhxa", 'password': "qjcmdhxa"}
    )
    return {"stato": "accesa"}

@app.post("/off")
def spegni():
    publish.single(
        TOPIC,
        "OFF",
        hostname="kebnekaise.lmq.cloudamqp.com",
        port=8883,
        tls={'ca_certs': None},
        auth={'username': "qjcmdhxa", 'password': "qjcmdhxa"}
    )
    return {"stato": "spenta"}
