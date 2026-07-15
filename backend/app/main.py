from fastapi import FastAPI
from app.config.settings import PROJECT_NAME, PROJECT_VERSION

app = FastAPI(
    title=PROJECT_NAME,
    version=PROJECT_VERSION
)

@app.get("/")
def home():
    return {
        "message": f"Welcome to {PROJECT_NAME}"
    }