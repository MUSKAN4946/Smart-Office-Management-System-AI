from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

from app.database.database import get_db

from app.models.employee import Employee
from app.models.department import Department
from app.models.attendance import Attendance
from app.models.leave import Leave
from app.models.payroll import Payroll

router = APIRouter(
    prefix="/pdf-report",
    tags=["PDF Report"]
)

@router.get("/")
def generate_pdf_report(db: Session = Depends(get_db)):

    total_employees = db.query(Employee).count()
    total_departments = db.query(Department).count()
    total_attendance = db.query(Attendance).count()
    total_leave = db.query(Leave).count()
    total_payroll = db.query(Payroll).count()

    pdf_file = "office_report.pdf"

    doc = SimpleDocTemplate(pdf_file)

    styles = getSampleStyleSheet()

    elements = []

    elements.append(
        Paragraph("<b>Smart Office Management System</b>", styles["Title"])
    )

    elements.append(
        Paragraph("Office Summary Report", styles["Heading2"])
    )

    elements.append(
        Paragraph(f"Total Employees : {total_employees}", styles["BodyText"])
    )

    elements.append(
        Paragraph(f"Departments : {total_departments}", styles["BodyText"])
    )

    elements.append(
        Paragraph(f"Attendance Records : {total_attendance}", styles["BodyText"])
    )

    elements.append(
        Paragraph(f"Leave Requests : {total_leave}", styles["BodyText"])
    )

    elements.append(
        Paragraph(f"Payroll Records : {total_payroll}", styles["BodyText"])
    )

    doc.build(elements)

    return FileResponse(
        pdf_file,
        media_type="application/pdf",
        filename="Office_Report.pdf"
    )