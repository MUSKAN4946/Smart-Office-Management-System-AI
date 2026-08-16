from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db

from app.schemas.dashboard_schema import (
    DashboardResponse,
    DepartmentEmployeeCountResponse,
    SalaryAnalyticsResponse
)

from app.services.dashboard_service import (
    get_dashboard_data,
    get_department_employee_count,
    get_salary_analytics
)

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get("/", response_model=DashboardResponse)
def dashboard(db: Session = Depends(get_db)):
    return get_dashboard_data(db)


@router.get(
    "/department-count",
    response_model=list[DepartmentEmployeeCountResponse]
)
def department_employee_count(
    db: Session = Depends(get_db)
):
    return get_department_employee_count(db)


@router.get(
    "/salary-analytics",
    response_model=SalaryAnalyticsResponse
)
def salary_analytics(
    db: Session = Depends(get_db)
):
    return get_salary_analytics(db)