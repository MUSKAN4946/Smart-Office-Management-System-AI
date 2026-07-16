from sqlalchemy import Column, Integer, String, Float, Boolean, Date

from app.database.database import Base


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)

    employee_code = Column(String(20), unique=True, nullable=False)

    full_name = Column(String(100), nullable=False)

    email = Column(String(100), unique=True, nullable=False)

    phone = Column(String(15))

    department = Column(String(100))

    designation = Column(String(100))

    joining_date = Column(Date)

    salary = Column(Float)

    is_active = Column(Boolean, default=True)