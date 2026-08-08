from sqlalchemy.orm import Session

from app.models.leave import Leave
from app.schemas.leave_schema import LeaveCreate


def create_leave(db: Session, leave: LeaveCreate):

    new_leave = Leave(
        employee_id=leave.employee_id,
        leave_type=leave.leave_type,
        start_date=leave.start_date,
        end_date=leave.end_date,
        reason=leave.reason
    )

    db.add(new_leave)
    db.commit()
    db.refresh(new_leave)

    return new_leave


def get_all_leaves(db: Session):

    return db.query(Leave).all()


def get_pending_leaves(db: Session):

    return db.query(Leave).filter(
        Leave.status == "Pending"
    ).all()


def approve_leave(
    db: Session,
    leave_id: int
):

    leave = db.query(Leave).filter(
        Leave.id == leave_id
    ).first()

    if leave is None:
        return None

    leave.status = "Approved"

    db.commit()
    db.refresh(leave)

    return leave

def reject_leave(
    db: Session,
    leave_id: int
):

    leave = db.query(Leave).filter(
        Leave.id == leave_id
    ).first()

    if leave is None:
        return None

    leave.status = "Rejected"

    db.commit()
    db.refresh(leave)

    return leave


def get_my_leaves(
    db: Session,
    employee_id: int
):

    return db.query(Leave).filter(
        Leave.employee_id == employee_id
    ).all()