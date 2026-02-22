import random
import time
import paho.mqtt.client as mqtt

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect("localhost", 1883)
client.loop_start()

while True:
    temp = random.randint(20, 35)
    client.publish("home/temperature", str(temp))
    print("Température envoyée :", temp)
    time.sleep(3)
