from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware

# Mostrar
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from pydantic import BaseModel, EmailStr, Field
from typing import Optional

# Instancia de la app
app = FastAPI(
    title="kitbox",
    description="multi herramienta de python",
    version="1.0.0",
    docs_url="/docs",      # Swagger UI
    redoc_url="/redoc",    # ReDoc
)


# CORS (permite peticiones desde tu frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],  # ajusta
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# CSS, JS, imágenes
app.mount("/static", StaticFiles(directory="static"), name="static")


# Rutas
@app.get("/")
async def index():
    """Devuelve la pantalla de inicio de sesión en la raíz."""
    return FileResponse("templates/index.html")



@app.get("/health", tags=["Root"])
def health_check():
    return {"status": "ok"}
