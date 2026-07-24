from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db

from app.models.employee import Employee
from app.models.department import Department
from app.models.attendance import Attendance
from app.models.leave import Leave
from app.models.payroll import Payroll

router = APIRouter(
    prefix="/office-statistics",
    tags=["Office Statistics"]
)


@router.get("/")
def office_statistics(db: Session = Depends(get_db)):

    total_employees = db.query(Employee).count()

    active_employees = db.query(Employee).filter(
        Employee.is_active == True
    ).count()

    inactive_employees = db.query(Employee).filter(
        Employee.is_active == False
    ).count()

    total_departments = db.query(Department).count()

    total_attendance_records = db.query(Attendance).count()

    total_leave_requests = db.query(Leave).count()

    total_payroll_records = db.query(Payroll).count()

    return {
    "total_employees": total_employees,
    "active_employees": active_employees,
    "inactive_employees": inactive_employees,
    "total_departments": total_departments,
    "total_attendance_records": total_attendance_records,
    "total_leave_requests": total_leave_requests,
    "total_payroll_records": total_payroll_records
}