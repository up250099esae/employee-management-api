from fastapi import FastAPI
from app.api.employees import router as employees_router

# Crea la aplicación web principal
app = FastAPI(
    title="Employee Management API",
    description="REST API for managing employees",
    version="1.0.0"
)

# Registra las rutas de employees.py dentro de la aplicación
app.include_router(employees_router)

# Ruta principal
@app.get("/")
def root():
    return {
        "message": "Welcome to the Employee Management API"
    } 

