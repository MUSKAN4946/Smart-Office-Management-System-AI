from pydantic import BaseModel


class DashboardResponse(BaseModel):
    total_employees: int
    active_employees: int
    inactive_employees: int

    total_departments: int

    total_attendance: int
    present_today: int
    absent_today: int

    total_leaves: int
    pending_leaves: int
    approved_leaves: int
    rejected_leaves: int

    total_payrolls: int

    total_users: int


class DepartmentEmployeeCountResponse(BaseModel):
    department: str
    employee_count: int


class SalaryAnalyticsResponse(BaseModel):
    total_salary_expense: float
    average_salary: float
    highest_salary: float
    lowest_salary: float