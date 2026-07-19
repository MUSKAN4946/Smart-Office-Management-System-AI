from sqlalchemy.orm import Session

from app.models.department import Department
from app.schemas.department_schema import DepartmentCreate


def create_department(db: Session, department: DepartmentCreate):

    new_department = Department(
        department_name=department.department_name,
        department_code=department.department_code,
        description=department.description
    )

    db.add(new_department)
    db.commit()
    db.refresh(new_department)

    return new_department


def get_all_departments(db: Session):

    return db.query(Department).all()