from sqlalchemy import Column, Integer, String, Float
from database import Base

class Flor(Base):

    __tablename__ = "flores"

    id = Column(Integer, primary_key=True, index=True)

    especie = Column(String, nullable=False)
    temporada = Column(String, nullable=False)

    #datos para ser capturados
    precio = Column(Float)
    wp = Column(Float)
    r400 = Column(Float)

    gif = Column(Float)
    insumo_b2b = Column(Float)

    precio_lista = Column(Float)

    #datos calculados :)
    costo_flete = Column(Float)
    gasto_venta = Column(Float)

    costo_base = Column(Float)
    costo_con_merma = Column(Float)

    precio_venta = Column(Float)

    utilidad_neta = Column(Float)
    utilidad_real = Column(Float)

    margen_real = Column(Float)