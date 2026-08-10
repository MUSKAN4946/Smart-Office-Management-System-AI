from datetime import date, time

from pydantic import BaseModel, field_validator

class AttendanceCreate(BaseModel):

    employee_id: int

    attendance_date: date

    check_in: time

    check_out: time | None = None

    status: str = "Present"

    @field_validator("status")
    @classmethod
    def validate_status(cls, value):

        allowed_statuses = [
            "Present",
            "Absent",
            "Half Day"
        ]

        if value not in allowed_statuses:
            raise ValueError(
                "Status must be Present, Absent, or Half Day"
            )

        return value


class AttendanceResponse(AttendanceCreate):

    id: int

    class Config:
        from_attributes = True