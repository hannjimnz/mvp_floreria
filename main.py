from fastapi import FastAPI

from database import engine, Base
from models.producto import Producto

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def inicio():
    return {"mensaje": "Sistema funcionando"}

#uvicorn main:app --reload   tiene que estar dentro del backend 
#http://127.0.0.1:8000/docs
