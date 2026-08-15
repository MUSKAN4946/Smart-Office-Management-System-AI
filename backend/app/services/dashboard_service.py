from datetime import date

from sqlalchemy.orm import Session
from sqlalchemy import func

from app.models.employee import Employee
from app.models.department import Department
from app.models.attendance import Attendance
from app.models.leave import Leave
from app.models.payroll import Payroll
from app.models.user import User



def get_dashboard_data(db: Session):

    return {
        "total_employees": db.query(Employee).count(),

        "active_employees": db.query(Employee).filter(
            Employee.is_active == True
        ).count(),

        "inactive_employees": db.query(Employee).filter(
            Employee.is_active == False
        ).count(),

        "total_departments": db.query(Department).count(),

        "total_attendance": db.query(Attendance).count(),

        "present_today": db.query(Attendance).filter(
            Attendance.attendance_date == date.today(),
            Attendance.status == "Present"
        ).count(),

        "absent_today": db.query(Attendance).filter(
            Attendance.attendance_date == date.today(),
            Attendance.status == "Absent"
        ).count(),

        "total_leaves": db.query(Leave).count(),

        "pending_leaves": db.query(Leave).filter(
            Leave.status == "Pending"
        ).count(),

        "approved_leaves": db.query(Leave).filter(
            Leave.status == "Approved"
        ).count(),

        "rejected_leaves": db.query(Leave).filter(
            Leave.status == "Rejected"
        ).count(),

        "total_payrolls": db.query(Payroll).count(),

        "total_users": db.query(User).count()
    }

def get_department_employee_count(db: Session):

    result = (
        db.query(
            Employee.department,
            func.count(Employee.id)
        )
        .group_by(Employee.department)
        .all()
    )

    return [
        {
            "department": department,
            "employee_count": count
        }
        for department, count in result
    ]


