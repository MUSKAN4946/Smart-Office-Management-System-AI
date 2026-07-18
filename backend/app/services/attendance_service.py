from sqlalchemy.orm import Session

from app.models.attendance import Attendance
from app.schemas.attendance_schema import AttendanceCreate


def create_attendance(
    db: Session,
    attendance: AttendanceCreate
):

    new_attendance = Attendance(
        employee_id=attendance.employee_id,
        attendance_date=attendance.attendance_date,
        check_in=attendance.check_in,
        check_out=attendance.check_out,
        status=attendance.status
    )

    db.add(new_attendance)
    db.commit()
    db.refresh(new_attendance)

    return new_attendance


def get_all_attendance(db: Session):

    return db.query(Attendance).all()