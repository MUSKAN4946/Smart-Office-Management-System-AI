from pydantic import BaseModel


class PayrollCreate(BaseModel):
    employee_id: int
    basic_salary: float
    hra: float
    bonus: float
    deductions: float
    net_salary: float


class PayrollResponse(BaseModel):
    id: int
    employee_id: int
    basic_salary: float
    hra: float
    bonus: float
    deductions: float
    net_salary: float

    class Config:
        from_attributes = True