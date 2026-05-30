from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import engine, Base, SessionLocal
from models.flor import Flor
from schemas.flor import FlorCreate, FlorResponse
from fastapi.middleware.cors import CORSMiddleware #lo tuvimos que agregar para arreglar algo del backend 

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # para desarrollo
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def inicio():
    return {"mensaje": "Sistema de costeo floral funcionando"}


@app.post("/flores", response_model=FlorResponse)
def crear_flor(flor: FlorCreate, db: Session = Depends(get_db)):

    # operacion para el costo del flete
    costo_flete = min(
        100 / flor.wp if flor.wp > 0 else 999,
        370 / flor.r400 if flor.r400 > 0 else 999
    )

    # gasto de la venta
    gasto_venta = flor.precio_lista * 0.05

    # costo base del producto
    costo_base = (
        flor.precio
        + costo_flete
        + flor.gif
        + flor.insumo_b2b
    )

    # costo de las mermas (realmente no se que sea eso, pero ahi ta )
    costo_con_merma = costo_base / 0.95

    # precio de la venta
    precio_venta = costo_con_merma / (1 - 0.35)

    # calculo para la utilidad neta
    utilidad_neta = precio_venta - costo_con_merma

    # calculo para la utilidad real
    utilidad_real = (
        flor.precio_lista
        - costo_con_merma
        - gasto_venta
    )

    # calculo para el margen real
    margen_real = (
        utilidad_real / flor.precio_lista
        if flor.precio_lista > 0
        else 0
    )

    nueva_flor = Flor(
        especie=flor.especie,
        temporada=flor.temporada,

        precio=flor.precio,
        wp=flor.wp,
        r400=flor.r400,

        gif=flor.gif,
        insumo_b2b=flor.insumo_b2b,

        precio_lista=flor.precio_lista,

        costo_flete=costo_flete,
        gasto_venta=gasto_venta,

        costo_base=costo_base,
        costo_con_merma=costo_con_merma,

        precio_venta=precio_venta,

        utilidad_neta=utilidad_neta,
        utilidad_real=utilidad_real,

        margen_real=margen_real
    )

    db.add(nueva_flor)
    db.commit()
    db.refresh(nueva_flor)

    return nueva_flor


@app.get("/flores", response_model=list[FlorResponse])
def listar_flores(db: Session = Depends(get_db)):
    return db.query(Flor).all()


@app.get("/flores/{flor_id}", response_model=FlorResponse)
def obtener_flor(flor_id: int, db: Session = Depends(get_db)):

    flor = db.query(Flor).filter(
        Flor.id == flor_id
    ).first()




#Con esto inicializamos nuestro proyecto amiguitos 
#uvicorn main:app --reload esete comando es para reiniciar el servidor,    tiene que estar dentro del backend (cd backend)
#http://127.0.0.1:8000/docs aqui encontraremos nuestra api

#http://localhost:5500/  aqui abriremos el front  jijjij
