# Script Python simula telemetría de autobuses, lanza mensajes cada 10 sewgundos

import time
import json
import random
from paho.mqtt import client as mqtt

BROKER = "34.175.70.12"   # IP o dominio del broker MQTT en GCP
PORT = 1883                        # O 8883 si usas TLS
TOPIC = "telemetria/autobuses"
CLIENT_ID = "simulador-autobus-001"

def generar_telemetria():
    return {
        "bus_id": f"BUS-{random.randint(1, 100)}",
        "timestamp": int(time.time()),
        "lat": round(random.uniform(40.4, 40.5), 6),  # Madrid aproximado
        "lon": round(random.uniform(-3.7, -3.6), 6),
        "velocidad_kmh": round(random.uniform(0, 80), 1),
        "temperatura_motor": round(random.uniform(70, 100), 1)
    }

def on_connect(client, userdata, flags, rc):
    print(f"Conectado al broker con código {rc}")

client = mqtt.Client(CLIENT_ID)
client.on_connect = on_connect

# Descomentar si se usa TLS
# client.tls_set()

client.connect(BROKER, PORT, 60)
client.loop_start()

while True:
    mensaje = json.dumps(generar_telemetria())
    client.publish(TOPIC, mensaje, qos=1)
    print(f"Publicado: {mensaje}")
    time.sleep(10)
