from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import engine, Base, SessionLocal
from models.producto import Producto
from schemas.producto import ProductoCreate, ProductoResponse

app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db 
    finally:
        db.close()

@app.get("/")
def inicio():
    return {"mensaje": "Sistema funcionando"}

@app.post ("/productos", response_model=ProductoResponse)
def crear_producto(producto: ProductoCreate, db: Session = Depends(get_db)):
    costo_total = (
        producto.costo_base
        + producto.mano_obra
        + producto.costos_indirectos 
        + producto.desperdicio 
    )

    precio_final = costo_total / (1 - producto.margen)
    utilidad = precio_final - costo_total

    nuevo_producto = Producto(
        nombre = producto.nombre, 
        costo_base= producto.costo_base, 
        mano_obra=producto.mano_obra,
        costos_indirectos=producto.costos_indirectos, 
        desperdicio = producto.desperdicio, 
        margen = producto.margen, 
        costo_total = costo_total, 
        precio_final=precio_final,
        utilidad = utilidad
         
    )

    db.add(nuevo_producto)
    db.commit()
    db.refresh(nuevo_producto)

    return nuevo_producto

@app.get("/productos", response_model=list[ProductoResponse])
def listar_productos(db: Session = Depends(get_db)):
    return db.querry(Producto).all()

#uvicorn main:app --reload   tiene que estar dentro del backend 
#http://127.0.0.1:8000/docs
