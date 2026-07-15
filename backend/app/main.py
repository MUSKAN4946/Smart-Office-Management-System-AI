from fastapi import FastAPI

app = FastAPI(
    title="Smart Office Management System with AI",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to Smart Office Management System with AI"
    }