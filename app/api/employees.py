from fastapi import APIRouter, HTTPException

from app.schemas.employee import EmployeeCreate, EmployeeUpdate


# We create a router for all the routes related to employees.
router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)

# Temporary database.
employees = [
    {
        "id": 1,
        "name": "Angel",
        "lastname": "Esparza",
        "email": "angel@example.com",
        "position": "Backend Developer",
        "salary": 50000,
        "status": "Active",
        "department": "IT",
        "hire_date": "2026-08-01"
    },
    {
        "id": 2,
        "name": "Valeria",
        "lastname": "Garces",
        "email": "valeria@example.com",
        "position": "HR Manager",
        "salary": 42000,
        "status": "Active",
        "department": "HR",
        "hire_date": "2026-07-15"
    }
]

# Return the complete list of employees.
@router.get("/")
def get_employees():
    return employees


# Return one employee by ID.
@router.get("/{employee_id}")
def get_employee(employee_id: int):
    employee = next(
        (emp for emp in employees if emp["id"] == employee_id),
        None
    )

    if employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return employee


# Create a new employee.
@router.post("/")
def create_employee(employee: EmployeeCreate):
    new_employee = {
        "id": len(employees) + 1,
        "name": employee.name,
        "lastname": employee.lastname,
        "email": employee.email,
        "position": employee.position,
        "salary": employee.salary,
        "status": employee.status,
        "department": employee.department,
        "hire_date": employee.hire_date
    }

    employees.append(new_employee)

    return new_employee

@router.put("/{employee_id}")
def update_employee(employee_id: int, employee: EmployeeUpdate):
    existing_employee = next(
        (emp for emp in employees if emp["id"] == employee_id),
        None
    )

    if existing_employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )
    update_data = employee.model_dump(exclude_unset=True)

    existing_employee.update(update_data)

    return existing_employee


@router.delete("/{employee_id}")
def delete_employee(employee_id:int): 
    existing_employee =next(
        (emp for emp in employees if emp["id"] == employee_id),
        None
    )
    if existing_employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )
    employees.remove(existing_employee)
    return { "message": "Employee deleted succesfully"}