from pydantic import BaseModel 

class ProductoCreate(BaseModel):
    nombre: str
    costo_base: float
    mano_obra: float
    costos_indirectos: float 
    desperdicio: float 
    margen: float 

class ProductoResponse(BaseModel):
    id: int 
    nombre: str

    costo_base: float 
    mano_obra: float 
    costos_indirectos: float 
    desperdicio: float 
    margen: float 

    costo_total: float 
    precio_final: float 
    utilidad: float 


class Config:
    from_attribures = True 