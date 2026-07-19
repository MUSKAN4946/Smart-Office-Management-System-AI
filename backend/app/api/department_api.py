from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.department_schema import (
    DepartmentCreate,
    DepartmentResponse
)
from app.services.department_service import (
    create_department,
    get_all_departments
)

router = APIRouter(
    prefix="/departments",
    tags=["Departments"]
)


@router.post("/", response_model=DepartmentResponse)
def add_department(
    department: DepartmentCreate,
    db: Session = Depends(get_db)
):
    return create_department(db, department)


@router.get("/", response_model=list[DepartmentResponse])
def fetch_departments(
    db: Session = Depends(get_db)
):
    return get_all_departments(db)