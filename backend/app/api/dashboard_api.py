from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db

from app.schemas.dashboard_schema import (
    DashboardResponse,
    DepartmentEmployeeCountResponse
)
from app.services.dashboard_service import (
    get_dashboard_data,
    get_department_employee_count
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