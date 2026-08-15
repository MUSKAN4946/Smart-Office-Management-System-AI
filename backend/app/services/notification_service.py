from sqlalchemy.orm import Session

from app.models.notification import Notification
from app.schemas.notification_schema import NotificationCreate


def create_notification(
    db: Session,
    notification: NotificationCreate
):

    new_notification = Notification(
        employee_id=notification.employee_id,
        title=notification.title,
        message=notification.message
    )

    db.add(new_notification)
    db.commit()
    db.refresh(new_notification)

    return new_notification


def get_my_notifications(
    db: Session,
    employee_id: int
):

    return db.query(Notification).filter(
        Notification.employee_id == employee_id
    ).all()


def mark_as_read(
    db: Session,
    notification_id: int
):

    notification = db.query(Notification).filter(
        Notification.id == notification_id
    ).first()

    if notification is None:
        return None

    notification.is_read = True

    db.commit()
    db.refresh(notification)

    return notification