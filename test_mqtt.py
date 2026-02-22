import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc, properties=None):
    print("Connecté au broker MQTT")
    client.subscribe("home/test")
    # on publie APRÈS la souscription
    client.publish("home/test", "Bonjour assistant domotique")

def on_message(client, userdata, msg):
    print("Message reçu :", msg.payload.decode())

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883)
client.loop_start()

time.sleep(3)

