from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.core.auth import get_current_user
from app.models.user import User

from app.schemas.employee_dashboard_schema import (
    EmployeeDashboardResponse
)

from app.services.employee_dashboard_service import (
    get_employee_dashboard
)


router = APIRouter(
    prefix="/employee-dashboard",
    tags=["Employee Dashboard"]
)


@router.get(
    "/",
    response_model=EmployeeDashboardResponse
)
def employee_dashboard(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    dashboard = get_employee_dashboard(
        db,
        current_user
    )

    if dashboard is None:
        raise HTTPException(
            status_code=404,
            detail="Employee profile not found"
        )

    return dashboard