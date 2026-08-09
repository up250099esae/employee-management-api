from datetime import date
from enum import Enum

from pydantic import BaseModel, EmailStr, Field


class EmployeeStatus(str, Enum):
    ACTIVE = "Active"
    INACTIVE = "Inactive"


class Department(str, Enum):
    IT = "IT"
    HR = "HR"
    FINANCE = "Finance"
    SALES = "Sales"


class EmployeeCreate(BaseModel):
    name: str = Field(min_length=2)
    lastname: str = Field(min_length=2)
    email: EmailStr
    position: str = Field(min_length=2)
    salary: float = Field(gt=0)
    status: EmployeeStatus
    department: Department
    hire_date: date
class EmployeeUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=2)
    lastname: str | None = Field(default=None, min_length=2)
    email: EmailStr | None = None
    position: str | None = Field(default=None, min_length=2)
    salary: float | None = Field(default=None, gt=0)
    status: EmployeeStatus | None = None
    department: Department | None = None
    hire_date: date | None = None
    department: Department | None
    hire_date: date | None