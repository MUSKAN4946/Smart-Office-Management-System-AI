from fastapi import APIRouter
from sqlalchemy import text

from app.database.database import engine
from app.config.settings import (
    PROJECT_NAME,
    PROJECT_VERSION
)

router = APIRouter(
    prefix="/health",
    tags=["Health"]
)


@router.get("/")
def health_check():

    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))

        database_status = "Connected"

    except Exception:
        database_status = "Disconnected"

    return {
        "status": "Running",
        "project": PROJECT_NAME,
        "version": PROJECT_VERSION,
        "database": database_status
    }