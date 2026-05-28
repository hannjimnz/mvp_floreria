from fastapi import FastAPI

from database import engine, Base
from models.producto import Producto

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def inicio():
    return {"mensaje": "Sistema funcionando"}