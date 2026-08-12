from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.role_checker import admin_required, employee_required
from app.database.database import get_db

from app.schemas.payroll_schema import (
    PayrollCreate,
    PayrollResponse
)

from app.services.payroll_service import (
    create_payroll,
    get_all_payrolls,
    get_employee_payroll
)


router = APIRouter(
    prefix="/payroll",
    tags=["Payroll"]
)


@router.post("/", response_model=PayrollResponse)
def add_payroll(
    payroll: PayrollCreate,
    db: Session = Depends(get_db),
    current_user=Depends(admin_required)
):
    return create_payroll(db, payroll)


@router.get("/", response_model=list[PayrollResponse])
def fetch_payrolls(
    db: Session = Depends(get_db)
):
    return get_all_payrolls(db)


@router.get("/my", response_model=list[PayrollResponse])
def fetch_my_payroll(
    db: Session = Depends(get_db),
    current_user=Depends(employee_required)
):
    return get_employee_payroll(
        db,
        current_user.email
    )