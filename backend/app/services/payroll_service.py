from sqlalchemy.orm import Session

from app.models.payroll import Payroll
from app.schemas.payroll_schema import PayrollCreate


def create_payroll(db: Session, payroll: PayrollCreate):

    new_payroll = Payroll(
        employee_id=payroll.employee_id,
        basic_salary=payroll.basic_salary,
        hra=payroll.hra,
        bonus=payroll.bonus,
        deductions=payroll.deductions,
        net_salary=payroll.net_salary
    )

    db.add(new_payroll)
    db.commit()
    db.refresh(new_payroll)

    return new_payroll


def get_all_payrolls(db: Session):

    return db.query(Payroll).all()