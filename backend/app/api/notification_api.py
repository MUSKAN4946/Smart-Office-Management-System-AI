from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.utils.role_checker import employee_required

from app.models.employee import Employee

from app.schemas.notification_schema import (
    NotificationCreate,
    NotificationResponse
)

from app.services.notification_service import (
    create_notification,
    get_my_notifications,
    mark_as_read
)

router = APIRouter(
    prefix="/notifications",
    tags=["Notifications"]
)


@router.post("/", response_model=NotificationResponse)
def add_notification(
    notification: NotificationCreate,
    db: Session = Depends(get_db)
):
    return create_notification(db, notification)


@router.get("/my", response_model=list[NotificationResponse])
def fetch_my_notifications(
    db: Session = Depends(get_db),
    current_user=Depends(employee_required)
):

    employee = db.query(Employee).filter(
        Employee.email == current_user.email
    ).first()

    if employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return get_my_notifications(
        db,
        employee.id
    )


@router.put("/{notification_id}/read",
            response_model=NotificationResponse)
def read_notification(
    notification_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(employee_required)
):

    notification = mark_as_read(
        db,
        notification_id
    )

    if notification is None:
        raise HTTPException(
            status_code=404,
            detail="Notification not found"
        )

    return notification