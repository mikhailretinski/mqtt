import paho.mqtt.client as mqtt
import time
from datetime import datetime

BROKER = "34.175.70.12"
PORT = 1883
TOPIC = "test/healthcheck"
CLIENT_ID = f"mqtt-healthcheck-{int(time.time())}"

# Mensaje
msg = f"✅ MQTT Python check desde EC2 — {datetime.utcnow().isoformat()}"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("✅ Conectado correctamente al broker")
        client.publish(TOPIC, msg)
        print(f"📤 Publicado: {TOPIC} → {msg}")
    else:
        print(f"❌ Fallo al conectar, código {rc}")

def on_publish(client, userdata, mid):
    print("✅ Publicación confirmada, cerrando conexión...")
    client.disconnect()

client = mqtt.Client(CLIENT_ID)
client.on_connect = on_connect
client.on_publish = on_publish

print(f"🔄 Conectando a {BROKER}:{PORT} como {CLIENT_ID}")
client.connect(BROKER, PORT, 60)
client.loop_forever()
