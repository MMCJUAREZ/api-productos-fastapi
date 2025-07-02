from fastapi import APIRouter
from models.request_models import SumaRequest
from services.operaciones_service import sumar,multiplicar

router = APIRouter()

@router.post("/suma")
def ruta_suma(datos: SumaRequest):
    resultado = sumar(datos.a, datos.b)
    return {"resultado": resultado}

@router.post("/multiplicar")
def ruta_multiplicar(datos: SumaRequest):
    resultado = multiplicar(datos.a, datos.b)
    return {"resultado": resultado}