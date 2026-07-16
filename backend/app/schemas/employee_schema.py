from pydantic import BaseModel
from datetime import date


class EmployeeCreate(BaseModel):
    employee_code: str
    full_name: str
    email: str
    phone: str
    department: str
    designation: str
    joining_date: date
    salary: float


class EmployeeResponse(EmployeeCreate):
    id: int
    is_active: bool

    class Config:
        from_attributes = True