from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.role_checker import (
    admin_required,
    employee_required
)
from app.database.database import get_db
from app.schemas.attendance_schema import (
    AttendanceCreate,
    AttendanceResponse
)
from app.services.attendance_service import (
    create_attendance,
    get_all_attendance,
    get_employee_attendance
)

router = APIRouter(
    prefix="/attendance",
    tags=["Attendance"]
)


@router.post("/", response_model=AttendanceResponse)
def add_attendance(
    attendance: AttendanceCreate,
    db: Session = Depends(get_db),
    current_user=Depends(admin_required)
):
    return create_attendance(db, attendance)


@router.get("/", response_model=list[AttendanceResponse])
def fetch_attendance(
    db: Session = Depends(get_db)
):
    return get_all_attendance(db)




@router.get("/my", response_model=list[AttendanceResponse])
def fetch_my_attendance(
    db: Session = Depends(get_db),
    current_user=Depends(employee_required)
):

   return get_employee_attendance(
    db,
    current_user.email
)