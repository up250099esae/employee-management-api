from fastapi import APIRouter, HTTPException, Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.schemas.employee import (
    EmployeeCreate,
    EmployeeUpdate,
    EmployeeSortField,
    SortOrder,
)
from app.database.connection import get_db
from app.models.employee import Employee


router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)


# Get all employees from PostgreSQL
@router.get("/")
def get_employees(
    department: str | None = None,
    status: str | None = None,
    name: str | None = None,
    sort_by: EmployeeSortField | None = None,
    order: SortOrder = SortOrder.ASC,
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=10, ge=1, le=100),
    db: Session = Depends(get_db)
):
    query = db.query(Employee)

    if department:
        query = query.filter(
            Employee.department.ilike(department)
        )

    if status:
        query = query.filter(
            Employee.status.ilike(status)
        )

    if name:
        query = query.filter(
            Employee.name.ilike(f"%{name}%")
        )

    allowed_sort_fields = {
        "name": Employee.name,
        "salary": Employee.salary,
        "hire_date": Employee.hire_date
    }

    if sort_by:
        sort_column = allowed_sort_fields[sort_by.value]

        if order == SortOrder.DESC:
            query = query.order_by(sort_column.desc())
        else:
            query = query.order_by(sort_column.asc())

    return query.offset(skip).limit(limit).all()


# Get one employee from PostgreSQL
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

    try:
        db.add(new_employee)
        db.commit()
        db.refresh(new_employee)

    except IntegrityError:
        db.rollback()

        raise HTTPException(
            status_code=409,
            detail="An employee with this email already exists"
        )

    return new_employee


# Update employee in PostgreSQL
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

    update_data = employee.model_dump(
        exclude_unset=True
    )

    for field, value in update_data.items():

        # Convert Enum values to normal strings
        if hasattr(value, "value"):
            value = value.value

        setattr(existing_employee, field, value)

    try:
        db.commit()
        db.refresh(existing_employee)

    except IntegrityError:
        db.rollback()

        raise HTTPException(
            status_code=409,
            detail="An employee with this email already exists"
        )

    return existing_employee


# Delete employee from PostgreSQL
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