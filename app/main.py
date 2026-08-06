# Importa la clase FastAPI de la librería FastAPI
from fastapi import FastAPI 
#crea la aplicacion web y todo lo que hagamos pertenecera a app
app = FastAPI(
    title="Employee Management API",
    description="REST API for managing employees",
    version="1.0.0"
)
# Esta función responde cuando alguien visita la ruta "/"
@app.get("/") 
def root():
    return {
        "message": "Welcome to the Employee Management API"
    }

