from fastapi import APIRouter

router = APIRouter(
    prefix="/email",
    tags=["Email Notification"]
)

@router.get("/")
def email_home():

    return {
        "message": "Email Notification Module is Ready"
    }