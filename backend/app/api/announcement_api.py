from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.announcement import Announcement

router = APIRouter(
    prefix="/announcements",
    tags=["Announcements"]
)

@router.get("/")
def get_announcements(db: Session = Depends(get_db)):

    announcements = db.query(Announcement).all()

    return announcements

@router.post("/")
def create_announcement(
    title: str,
    message: str,
    db: Session = Depends(get_db)
):

    announcement = Announcement(
        title=title,
        message=message
    )

    db.add(announcement)
    db.commit()
    db.refresh(announcement)

    return {
        "message": "Announcement Created Successfully",
        "announcement": announcement
    }

@router.delete("/{announcement_id}")
def delete_announcement(
    announcement_id: int,
    db: Session = Depends(get_db)
):

    announcement = db.query(Announcement).filter(
        Announcement.id == announcement_id
    ).first()

    if not announcement:
        return {
            "message": "Announcement Not Found"
        }

    db.delete(announcement)
    db.commit()

    return {
        "message": "Announcement Deleted Successfully"
    }