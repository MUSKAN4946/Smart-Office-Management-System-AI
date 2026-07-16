from fastapi import FastAPI

from app.config.settings import PROJECT_NAME, PROJECT_VERSION
from app.database.database import engine

app = FastAPI(
    title=PROJECT_NAME,
    version=PROJECT_VERSION
)


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