from sqlalchemy.orm import Session

from app.models.employee import Employee
from app.models.attendance import Attendance
from app.models.leave import Leave
from app.models.payroll import Payroll
from app.models.user import User


def get_employee_dashboard(
    db: Session,
    current_user: User
):

    employee = db.query(Employee).filter(
        Employee.email == current_user.email
    ).first()

    if employee is None:
        return None

    attendance_count = db.query(Attendance).filter(
        Attendance.employee_id == employee.id
    ).count()

    leave_count = db.query(Leave).filter(
        Leave.employee_id == employee.id
    ).count()

    payroll_count = db.query(Payroll).filter(
        Payroll.employee_id == employee.id
    ).count()

    return {
        "employee": employee,
        "attendance_count": attendance_count,
        "leave_count": leave_count,
        "payroll_count": payroll_count
    }