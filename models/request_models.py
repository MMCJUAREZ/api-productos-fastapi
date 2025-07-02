from pydantic import BaseModel

class ProductoRequest(BaseModel):
    nombre: str
    precio: float

class ProductoResponse(ProductoRequest):
    id: int

    class Config:
        orm_mode = True
