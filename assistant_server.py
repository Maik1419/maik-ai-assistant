from fastapi import FastAPI

app = FastAPI()

@app.get("/ask")
def ask(q: str):
    return {
        "response": f"Tu as demandé : '{q}'. Ceci est une réponse simulée (mode gratuit)."
    }