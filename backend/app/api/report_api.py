from fastapi import APIRouter, Depends
from datetime import datetime
from sqlalchemy.orm import Session

from app.database.database import get_db

from app.models.employee import Employee
from app.models.department import Department
from app.models.attendance import Attendance
from app.models.leave import Leave
from app.models.payroll import Payroll

router = APIRouter(
    prefix="/reports",
    tags=["Reports"]
)

@router.get("/")
def generate_report(db: Session = Depends(get_db)):

    total_employees = db.query(Employee).count()

    total_departments = db.query(Department).count()

    total_attendance = db.query(Attendance).count()

    total_leaves = db.query(Leave).count()

    total_payroll = db.query(Payroll).count()

    return {
    "report_name": "Office Summary Report",
    "generated_on": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
    "generated_by": "Smart Office Management System",
    "report_status": "Generated Successfully",

    "employees": total_employees,
    "departments": total_departments,
    "attendance_records": total_attendance,
    "leave_requests": total_leaves,
    "payroll_records": total_payroll
}