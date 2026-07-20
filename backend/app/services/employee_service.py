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


def get_all_employees(
    db: Session,
    search: str = None,
    department: str = None,
    skip: int = 0,
    limit: int = 10,
    sort_by: str = "id"
):

    query = db.query(Employee)

    if search:
        query = query.filter(
            Employee.full_name.ilike(f"%{search}%")
        )

    if department:
        query = query.filter(
            Employee.department.ilike(f"%{department}%")
        )

    if sort_by == "name":
        query = query.order_by(Employee.full_name)

    elif sort_by == "salary":
        query = query.order_by(Employee.salary.desc())

    else:
        query = query.order_by(Employee.id)

    return query.offset(skip).limit(limit).all()


def get_employee_by_id(db: Session, employee_id: int):
    return db.query(Employee).filter(Employee.id == employee_id).first()


def update_employee(
    db: Session,
    employee_id: int,
    employee: EmployeeCreate
):

    existing_employee = db.query(Employee).filter(
        Employee.id == employee_id
    ).first()

    if not existing_employee:
        return None

    existing_employee.employee_code = employee.employee_code
    existing_employee.full_name = employee.full_name
    existing_employee.email = employee.email
    existing_employee.phone = employee.phone
    existing_employee.department = employee.department
    existing_employee.designation = employee.designation
    existing_employee.joining_date = employee.joining_date
    existing_employee.salary = employee.salary

    db.commit()
    db.refresh(existing_employee)

    return existing_employee


def delete_employee(db: Session, employee_id: int):

    employee = db.query(Employee).filter(
        Employee.id == employee_id
    ).first()

    if not employee:
        return None

    db.delete(employee)
    db.commit()

    return {"message": "Employee deleted successfully"}