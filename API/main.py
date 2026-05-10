"""
API REST para predicción de cáncer de mama
Jose Espinoza y Jorge Bello
"""
from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from routes.predict import router, load_model_and_scaler 



@asynccontextmanager
async def lifespan(app: FastAPI):
    load_model_and_scaler()
    print("✓ API lista")
    yield
    print("✓ API detenida")

# Crear aplicación FastAPI
app = FastAPI(
    title="API de Predicción de Cáncer de Mama",
    description="Sistema de clasificación de tumores de mama como malignos o benignos",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Incluir rutas
app.include_router(router)


@app.get("/")
async def root():
    """Endpoint raíz"""
    return {
        "mensaje": "Bienvenido a la API de predicción de cáncer de mama",
        "documentacion": "/docs",
        "redoc": "/redoc"
    }


@app.get("/info")
async def info():
    """Información del proyecto"""
    return {
        "proyecto": "Clasificación de Tumores de Mama",
        "objetivo": "Clasificar tumores como malignos (M) o benignos (B)",
        "versión": "1.0.0",
        "endpoints": {
            "POST /predict": "Realizar predicción",
            "GET /health": "Verificar estado",
            "GET /docs": "Documentación interactiva (Swagger)"
        }
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
