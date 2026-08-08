from datetime import date
from pydantic import BaseModel


class EmployeeDashboardProfile(BaseModel):

    id: int
    employee_code: str
    full_name: str
    email: str
    phone: str | None = None
    department: str | None = None
    designation: str | None = None
    joining_date: date | None = None
    salary: float | None = None
    is_active: bool

    class Config:
        from_attributes = True


class EmployeeDashboardResponse(BaseModel):

    employee: EmployeeDashboardProfile

    attendance_count: int

    leave_count: int

    payroll_count: int