from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.schemas.employee import EmployeeCreate, EmployeeUpdate
from app.database.connection import get_db
from app.models.employee import Employee


router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)





# Get all employees from PostgreSQL
@router.get("/")
def get_employees(db: Session = Depends(get_db)):
    database_employees = db.query(Employee).all()
    return database_employees


# Get one employee from temporary database
@router.get("/{employee_id}")
def get_employee(
    employee_id: int,
    db: Session = Depends(get_db)
):
    employee = db.query(Employee).filter(
        Employee.id == employee_id
    ).first()

    if employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return employee


# Create employee in PostgreSQL
@router.post("/")
def create_employee(
    employee: EmployeeCreate,
    db: Session = Depends(get_db)
):
    new_employee = Employee(
        name=employee.name,
        lastname=employee.lastname,
        email=employee.email,
        position=employee.position,
        salary=employee.salary,
        status=employee.status.value,
        department=employee.department.value,
        hire_date=employee.hire_date,
        phone=employee.phone
    )

    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)

    return new_employee


# Update employee in temporary database
@router.put("/{employee_id}")
def update_employee(
    employee_id: int,
    employee: EmployeeUpdate,
    db: Session = Depends(get_db)
):
    existing_employee = db.query(Employee).filter(
        Employee.id == employee_id
    ).first()

    if existing_employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    update_data = employee.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(existing_employee, field, value)

    db.commit()
    db.refresh(existing_employee)

    return existing_employee


# Delete employee from temporary database
@router.delete("/{employee_id}")
def delete_employee(
    employee_id: int,
    db: Session = Depends(get_db)
):
    existing_employee = db.query(Employee).filter(
        Employee.id == employee_id
    ).first()

    if existing_employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    db.delete(existing_employee)
    db.commit()

    return {
        "message": "Employee deleted successfully"
    }