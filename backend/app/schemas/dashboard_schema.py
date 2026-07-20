from pydantic import BaseModel


class DashboardResponse(BaseModel):
    total_employees: int
    total_departments: int
    total_attendance: int
    total_leaves: int
    total_payrolls: int
    total_users: int