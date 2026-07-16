from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.employee_schema import EmployeeCreate, EmployeeResponse
from app.services.employee_service import (
    create_employee,
    get_all_employees
)

from app.services.auth_service import get_current_user
from app.models.user import User

router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)


@router.post("/", response_model=EmployeeResponse)
def add_employee(
    employee: EmployeeCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return create_employee(db, employee)


@router.get("/", response_model=list[EmployeeResponse])
def fetch_employees(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return get_all_employees(db)