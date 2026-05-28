from sqlalchemy import Column, Integer, String, Float
from database import Base

class Producto(Base):

    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, index=True)

    nombre = Column(String, nullable=False)

    costo_base = Column(Float)
    mano_obra = Column(Float)
    costos_indirectos = Column(Float)
    desperdicio = Column(Float)

    margen = Column(Float)

    costo_total = Column(Float)
    precio_final = Column(Float)
    utilidad = Column(Float)