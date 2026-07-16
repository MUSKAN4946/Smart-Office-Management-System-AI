from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user_schema import UserRegister
from app.utils.hashing import hash_password, verify_password

from app.core.jwt_handler import create_access_token


def register_user(db: Session, user: UserRegister):

    hashed_password = hash_password(user.password)

    new_user = User(
        full_name=user.full_name,
        email=user.email,
        password=hashed_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def login_user(db: Session, email: str, password: str):

    user = db.query(User).filter(User.email == email).first()

    if user is None:
        return None

    if not verify_password(password, user.password):
        return False

    access_token = create_access_token(
        data={
            "sub": user.email,
            "role": user.role
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": user
    }