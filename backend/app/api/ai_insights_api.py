from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db

from app.models.employee import Employee
from app.models.attendance import Attendance


router = APIRouter(
    prefix="/ai-insights",
    tags=["AI Insights"]
)


@router.get("/")
def ai_employee_insights(db: Session = Depends(get_db)):

    total_employees = db.query(Employee).count()

    total_attendance = db.query(Attendance).count()

    if total_employees == 0:
        return {
            "message": "No employees found."
        }

    average_attendance = total_attendance / total_employees

    if average_attendance >= 20:
        insight = "Excellent Attendance"
        recommendation = "Eligible for Employee of the Month"

    elif average_attendance >= 10:
        insight = "Good Attendance"
        recommendation = "Maintain Consistency"

    else:
        insight = "Low Attendance"
        recommendation = "Needs Improvement"

    return {
        "total_employees": total_employees,
        "total_attendance_records": total_attendance,
        "average_attendance": round(average_attendance, 2),
        "ai_insight": insight,
        "recommendation": recommendation
    }