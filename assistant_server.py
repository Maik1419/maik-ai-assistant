from fastapi import FastAPI
import paho.mqtt.publish as publish
import os
from openai import OpenAI

app = FastAPI()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

MQTT_BROKER = "localhost"
MQTT_TOPIC = "maison/lumiere"


@app.get("/ask")
def ask(q: str):

    q_lower = q.lower()

    if "allume" in q_lower:
        publish.single(MQTT_TOPIC, "ON", hostname=MQTT_BROKER)
        return {"response": "Lumière allumée"}

    elif "eteins" in q_lower or "éteins" in q_lower:
        publish.single(MQTT_TOPIC, "OFF", hostname=MQTT_BROKER)
        return {"response": "Lumière éteinte"}

    else:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Tu es un assistant domotique intelligent."},
                {"role": "user", "content": q}
            ]
        )

        answer = response.choices[0].message.content
        return {"response": answer}