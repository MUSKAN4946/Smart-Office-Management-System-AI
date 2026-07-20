from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.payroll_schema import (
    PayrollCreate,
    PayrollResponse
)
from app.services.payroll_service import (
    create_payroll,
    get_all_payrolls
)

router = APIRouter(
    prefix="/payroll",
    tags=["Payroll"]
)






@router.post("/", response_model=PayrollResponse)
def add_payroll(
    payroll: PayrollCreate,
    db: Session = Depends(get_db)
):
    return create_payroll(db, payroll)


@router.get("/", response_model=list[PayrollResponse])
def fetch_payrolls(
    db: Session = Depends(get_db)
):
    return get_all_payrolls(db)