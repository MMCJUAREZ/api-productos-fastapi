from fastapi import FastAPI
from routers import calculadora_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Calculadora API FastAPI",
              description="API REST para operaciones matemáticas básicas",
              version="1.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def inicio():
    return {"mensaje": "Bienvenido a la Calculadora API"}

# Incluir rutas desde el router
app.include_router(calculadora_router.router, prefix="/calculadora", tags=["Operaciones"])
