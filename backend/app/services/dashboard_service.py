from sqlalchemy.orm import Session

from app.models.employee import Employee
from app.models.department import Department
from app.models.attendance import Attendance
from app.models.leave import Leave
from app.models.payroll import Payroll
from app.models.user import User


def get_dashboard_data(db: Session):

    return {
        "total_employees": db.query(Employee).count(),
        "total_departments": db.query(Department).count(),
        "total_attendance": db.query(Attendance).count(),
        "total_leaves": db.query(Leave).count(),
        "total_payrolls": db.query(Payroll).count(),
        "total_users": db.query(User).count()
    }