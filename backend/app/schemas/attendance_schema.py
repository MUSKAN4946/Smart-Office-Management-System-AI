from datetime import date, time

from pydantic import BaseModel


class AttendanceCreate(BaseModel):

    employee_id: int

    attendance_date: date

    check_in: time

    check_out: time | None = None

    status: str = "Present"


class AttendanceResponse(AttendanceCreate):

    id: int

    class Config:
        from_attributes = True