from sqlalchemy import Column, Integer, Float, ForeignKey

from app.database.database import Base


class Payroll(Base):
    __tablename__ = "payroll"

    id = Column(Integer, primary_key=True, index=True)

    employee_id = Column(
        Integer,
        ForeignKey("employees.id"),
        nullable=False
    )

    basic_salary = Column(Float, nullable=False)

    hra = Column(Float, default=0)

    bonus = Column(Float, default=0)

    deductions = Column(Float, default=0)

    net_salary = Column(Float, nullable=False)