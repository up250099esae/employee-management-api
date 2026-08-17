from fastapi import FastAPI

from app.api.employees import router as employees_router
from app.database.connection import Base, engine
from app.models.employee import Employee


app = FastAPI(
    title="Employee Management API",
    description="REST API for managing employees",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

app.include_router(employees_router)


@app.get("/")
def root():
    return {
        "message": "Welcome to the Employee Management API"
    }

