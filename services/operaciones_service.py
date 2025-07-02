from fastapi import HTTPException
from typing import List, Optional
from models.request_models import ProductoRequest, ProductoResponse

class ProductoService:
    def __init__(self):
        self.productos: List[ProductoResponse] = []
        self.id_actual = 1

    def get_productos(self) -> List[ProductoResponse]:
        return self.productos

    def get_producto(self, producto_id: int) -> Optional[ProductoResponse]:
        return next((p for p in self.productos if p.id == producto_id), None)

    def create_producto(self, producto: ProductoRequest) -> ProductoResponse:
        nuevo = ProductoResponse(id=self.id_actual, **producto.dict())
        self.productos.append(nuevo)
        self.id_actual += 1
        return nuevo

    def update_producto(self, producto_id: int, producto: ProductoRequest) -> Optional[ProductoResponse]:
        prod = self.get_producto(producto_id)
        if prod:
            prod.nombre = producto.nombre
            prod.precio = producto.precio
            return prod
        return None

    def delete_producto(self, producto_id: int) -> bool:
        prod = self.get_producto(producto_id)
        if prod:
            self.productos.remove(prod)
            return True
        return False