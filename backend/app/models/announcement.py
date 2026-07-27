from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from app.database.database import Base


class Announcement(Base):
    __tablename__ = "announcements"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String(150), nullable=False)

    message = Column(String(500), nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)