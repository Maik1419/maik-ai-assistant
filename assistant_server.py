from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

app = FastAPI()

# Base de données SQLite
DATABASE_URL = "sqlite:///./memory.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


# Modèle Message
class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)


# Créer la table
Base.metadata.create_all(bind=engine)


@app.get("/ask")
def ask(q: str):
    db = SessionLocal()

    # Sauvegarder le message
    new_message = Message(content=q)
    db.add(new_message)
    db.commit()

    # Compter le nombre total de messages
    count = db.query(Message).count()

    db.close()

    return {
        "response": f"Message enregistré. Total messages : {count}"
    }