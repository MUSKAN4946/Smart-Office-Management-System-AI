from fastapi import FastAPI

from app.config.settings import PROJECT_NAME, PROJECT_VERSION
from app.database.database import Base, engine

# Models
from app.models.employee import Employee
from app.models.user import User
from app.models.attendance import Attendance
from app.models.leave import Leave

# APIs
from app.api.employee_api import router as employee_router
from app.api.user_api import router as user_router
from app.api.attendance_api import router as attendance_router
from app.api.leave_api import router as leave_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=PROJECT_NAME,
    version=PROJECT_VERSION
)

# Register APIs
app.include_router(employee_router)
app.include_router(user_router)
app.include_router(attendance_router)
app.include_router(leave_router)


@app.get("/")
def home():
    return {
        "message": f"Welcome to {PROJECT_NAME}"
    }


@app.get("/database")
def database_check():
    try:
        connection = engine.connect()
        connection.close()

        return {
            "status": "Database Connected Successfully"
        }

    except Exception as e:
        return {
            "status": "Connection Failed",
            "error": str(e)
        }