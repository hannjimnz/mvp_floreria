from pydantic import BaseModel 

class FlorCreate(BaseModel):

    especie: str
    temporada: str

    precio: float
    wp: float
    r400: float

    gif: float
    insumo_b2b: float

    precio_lista: float


class FlorResponse(BaseModel):

    id: int

    especie: str
    temporada: str

    precio: float
    wp: float
    r400: float

    gif: float
    insumo_b2b: float

    precio_lista: float

    costo_flete: float
    gasto_venta: float

    costo_base: float
    costo_con_merma: float

    precio_venta: float

    utilidad_neta: float
    utilidad_real: float

    margen_real: float

    class Config:
        from_attributes = True