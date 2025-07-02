from fastapi import APIRouter, HTTPException
from models.request_models import ProductoRequest, ProductoResponse
from services.operaciones_service import ProductoService

router = APIRouter()
service = ProductoService()

@router.get("/", response_model=list[ProductoResponse])
def listar_productos():
    return service.get_productos()

@router.get("/{producto_id}", response_model=ProductoResponse)
def obtener_producto(producto_id: int):
    prod = service.get_producto(producto_id)
    if not prod:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return prod

@router.post("/", response_model=ProductoResponse)
def crear_producto(producto: ProductoRequest):
    return service.create_producto(producto)

@router.put("/{producto_id}", response_model=ProductoResponse)
def actualizar_producto(producto_id: int, producto: ProductoRequest):
    prod = service.update_producto(producto_id, producto)
    if not prod:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return prod

@router.delete("/{producto_id}")
def eliminar_producto(producto_id: int):
    if not service.delete_producto(producto_id):
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return {"detail": "Producto eliminado"}