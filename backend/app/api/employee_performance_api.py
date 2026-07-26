from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db

from app.models.employee import Employee
from app.models.attendance import Attendance

router = APIRouter(
    prefix="/employee-performance",
    tags=["Employee Performance"]
)

@router.get("/")
def employee_performance(db: Session = Depends(get_db)):

    total_employees = db.query(Employee).count()

    total_attendance = db.query(Attendance).count()

    if total_employees == 0:
        return {
            "message": "No employees found."
        }

    average_attendance = total_attendance / total_employees

    performance_score = round((average_attendance / 30) * 100)

    if performance_score >= 90:
        performance_level = "Excellent"
        recommendation = "Eligible for Promotion"

    elif performance_score >= 70:
        performance_level = "Good"
        recommendation = "Keep Improving"

    elif performance_score >= 50:
        performance_level = "Average"
        recommendation = "Needs Better Attendance"

    else:
        performance_level = "Poor"
        recommendation = "Immediate Improvement Required"

    return {
        "total_employees": total_employees,
        "total_attendance_records": total_attendance,
        "average_attendance": round(average_attendance, 2),
        "performance_score": performance_score,
        "performance_level": performance_level,
        "recommendation": recommendation
    }