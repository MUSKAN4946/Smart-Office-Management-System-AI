from sqlalchemy import Column, Integer, Date, Time, ForeignKey, String
from sqlalchemy.orm import relationship

from app.database.database import Base


class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True, index=True)

    employee_id = Column(
        Integer,
        ForeignKey("employees.id"),
        nullable=False
    )

    attendance_date = Column(Date, nullable=False)

    check_in = Column(Time, nullable=False)

    check_out = Column(Time)

    status = Column(String(20), default="Present")

    employee = relationship(
        "Employee",
        back_populates="attendances"
    )