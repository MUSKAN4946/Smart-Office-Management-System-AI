from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from openpyxl import Workbook

from app.database.database import get_db

from app.models.employee import Employee
from app.models.department import Department
from app.models.attendance import Attendance
from app.models.leave import Leave
from app.models.payroll import Payroll

router = APIRouter(
    prefix="/excel-report",
    tags=["Excel Report"]
)

@router.get("/")
def generate_excel_report(db: Session = Depends(get_db)):

    total_employees = db.query(Employee).count()
    total_departments = db.query(Department).count()
    total_attendance = db.query(Attendance).count()
    total_leave = db.query(Leave).count()
    total_payroll = db.query(Payroll).count()

    workbook = Workbook()

    sheet = workbook.active

    sheet.title = "Office Report"

    sheet.append(["Smart Office Management System"])
    sheet.append([])

    sheet.append(["Category", "Count"])

    sheet.append(["Total Employees", total_employees])
    sheet.append(["Departments", total_departments])
    sheet.append(["Attendance Records", total_attendance])
    sheet.append(["Leave Requests", total_leave])
    sheet.append(["Payroll Records", total_payroll])

    excel_file = "Office_Report.xlsx"

    workbook.save(excel_file)

    return FileResponse(
        path=excel_file,
        filename="Office_Report.xlsx",
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )