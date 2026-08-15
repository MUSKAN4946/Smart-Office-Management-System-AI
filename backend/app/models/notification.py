from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from app.database.database import Base


class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True)

    employee_id = Column(
        Integer,
        ForeignKey("employees.id"),
        nullable=False
    )

    title = Column(String(100), nullable=False)

    message = Column(String(255), nullable=False)

    is_read = Column(Boolean, default=False)

    employee = relationship(
        "Employee",
        back_populates="notifications"
    )