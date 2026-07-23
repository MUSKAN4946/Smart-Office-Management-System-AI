from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.core.role_checker import admin_required

from app.schemas.employee_schema import EmployeeCreate, EmployeeResponse
from app.services.employee_service import (
    create_employee,
    get_all_employees,
    get_employee_by_id,
    update_employee,
    delete_employee
)

router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)


@router.post("/", response_model=EmployeeResponse)
def add_employee(
    employee: EmployeeCreate,
    db: Session = Depends(get_db),
    current_user=Depends(admin_required)
):
    return create_employee(db, employee)


@router.get("/", response_model=list[EmployeeResponse])
def fetch_employees(
    search: str = None,
    department: str = None,
    skip: int = 0,
    limit: int = 10,
    sort_by: str = "id",
    db: Session = Depends(get_db)
):
    return get_all_employees(
        db=db,
        search=search,
        department=department,
        skip=skip,
        limit=limit,
        sort_by=sort_by
    )


@router.get("/{employee_id}", response_model=EmployeeResponse)
def fetch_employee_by_id(
    employee_id: int,
    db: Session = Depends(get_db)
):
    employee = get_employee_by_id(db, employee_id)

    if employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return employee


@router.put("/{employee_id}", response_model=EmployeeResponse)
def edit_employee(
    employee_id: int,
    employee: EmployeeCreate,
    db: Session = Depends(get_db),
    current_user=Depends(admin_required)
):
    updated_employee = update_employee(
        db,
        employee_id,
        employee
    )

    if updated_employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return updated_employee


@router.delete("/{employee_id}")
def remove_employee(
    employee_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(admin_required)
):
    deleted_employee = delete_employee(
        db,
        employee_id
    )

    if deleted_employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return deleted_employee