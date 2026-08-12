from fastapi import APIRouter, Depends, HTTPException
from app.models.employee import Employee

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.role_checker import (
    admin_required,
    employee_required
)

from app.database.database import get_db
from app.schemas.leave_schema import (
    LeaveCreate,
    LeaveResponse
)
from app.services.leave_service import (
    create_leave,
    get_all_leaves,
    get_pending_leaves,
    approve_leave,
    reject_leave,
    get_my_leaves
)



router = APIRouter(
    prefix="/leaves",
    tags=["Leaves"]
)


@router.post("/", response_model=LeaveResponse)
def add_leave(
    leave: LeaveCreate,
    db: Session = Depends(get_db),
    current_user=Depends(employee_required)

):
    return create_leave(db, leave)


@router.get("/", response_model=list[LeaveResponse])
def fetch_leaves(
    db: Session = Depends(get_db),
    current_user=Depends(admin_required)
):
    return get_all_leaves(db)


@router.get("/my", response_model=list[LeaveResponse])
def fetch_my_leaves(
    db: Session = Depends(get_db),
    current_user=Depends(employee_required)
):

    employee = db.query(Employee).filter(
        Employee.email == current_user.email
    ).first()

    if employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return get_my_leaves(
        db,
        employee.id
    )





@router.get("/pending", response_model=list[LeaveResponse])
def fetch_pending_leaves(
    db: Session = Depends(get_db),
    current_user=Depends(admin_required)
):
    return get_pending_leaves(db)


@router.put("/{leave_id}/approve", response_model=LeaveResponse)
def approve_leave_request(
    leave_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(admin_required)
):

    leave = approve_leave(db, leave_id)

    if leave is None:
        raise HTTPException(
            status_code=404,
            detail="Leave Request Not Found"
        )

    return leave


@router.put("/{leave_id}/reject", response_model=LeaveResponse)
def reject_leave_request(
    leave_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(admin_required)
):

    leave = reject_leave(db, leave_id)

    if leave is None:
        raise HTTPException(
            status_code=404,
            detail="Leave Request Not Found"
        )

    return leave