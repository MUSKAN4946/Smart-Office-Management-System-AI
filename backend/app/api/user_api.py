from app.models.user import User
from app.utils.role_checker import admin_required

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.user_schema import UserRegister, UserResponse
from app.services.user_service import (
    register_user,
    login_user
)

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post("/register", response_model=UserResponse)
def create_user(user: UserRegister, db: Session = Depends(get_db)):
    return register_user(db, user)


@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    result = login_user(
        db,
        form_data.username,
        form_data.password
    )

    if result is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    if result is False:
        raise HTTPException(
            status_code=401,
            detail="Incorrect Password"
        )

    return {
        "access_token": result["access_token"],
        "token_type": result["token_type"],
        "user": {
            "id": result["user"].id,
            "full_name": result["user"].full_name,
            "email": result["user"].email,
            "role": result["user"].role
        }
    }


@router.put("/{user_id}/role")
def update_user_role(
    user_id: int,
    role: str,
    db: Session = Depends(get_db),
    current_user=Depends(admin_required)
):
    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    if role not in ["Admin", "Employee"]:
        raise HTTPException(
            status_code=400,
            detail="Role must be Admin or Employee"
        )

    user.role = role

    db.commit()
    db.refresh(user)

    return {
        "message": "User role updated successfully",
        "user_id": user.id,
        "email": user.email,
        "role": user.role
    }