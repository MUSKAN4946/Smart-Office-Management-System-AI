from sqlalchemy.orm import Session

from app.models.employee import Employee
from app.schemas.employee_schema import EmployeeCreate


def create_employee(db: Session, employee: EmployeeCreate):

    new_employee = Employee(
        employee_code=employee.employee_code,
        full_name=employee.full_name,
        email=employee.email,
        phone=employee.phone,
        department=employee.department,
        designation=employee.designation,
        joining_date=employee.joining_date,
        salary=employee.salary
    )

    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)

    return new_employee

def get_all_employees(db: Session):
    return db.query(Employee).all()