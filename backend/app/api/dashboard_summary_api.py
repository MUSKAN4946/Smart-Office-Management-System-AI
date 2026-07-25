from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db

from app.models.employee import Employee
from app.models.department import Department
from app.models.attendance import Attendance
from app.models.leave import Leave

router = APIRouter(
    prefix="/dashboard-summary",
    tags=["Dashboard Summary"]
)

@router.get("/")
def dashboard_summary(db: Session = Depends(get_db)):

    total_employees = db.query(Employee).count()

    total_departments = db.query(Department).count()

    total_attendance = db.query(Attendance).count()

    total_leave_requests = db.query(Leave).count()

    active_employees = db.query(Employee).filter(
        Employee.is_active == True
    ).count()

    return {
        "dashboard_title": "Smart Office Dashboard",

        "total_employees": total_employees,

        "active_employees": active_employees,

        "total_departments": total_departments,

        "attendance_records": total_attendance,

        "leave_requests": total_leave_requests,

        "status": "Dashboard Loaded Successfully"
    }