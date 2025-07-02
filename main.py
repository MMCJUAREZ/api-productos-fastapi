from fastapi import FastAPI
from routers import calculadora_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="API Productos FastAPI",
    description="API REST para gestión de productos en memoria",
    version="1.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def inicio():
    return {"mensaje": "Bienvenido a la API de Productos"}

# Incluir rutas desde el router
app.include_router(calculadora_router.router, prefix="/productos", tags=["Productos"])
