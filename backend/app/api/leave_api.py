from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.leave_schema import (
    LeaveCreate,
    LeaveResponse
)
from app.services.leave_service import (
    create_leave,
    get_all_leaves
)

router = APIRouter(
    prefix="/leaves",
    tags=["Leaves"]
)


@router.post("/", response_model=LeaveResponse)
def add_leave(
    leave: LeaveCreate,
    db: Session = Depends(get_db)
):
    return create_leave(db, leave)


@router.get("/", response_model=list[LeaveResponse])
def fetch_leaves(
    db: Session = Depends(get_db)
):
    return get_all_leaves(db)