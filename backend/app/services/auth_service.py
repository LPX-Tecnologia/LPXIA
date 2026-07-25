from sqlalchemy.orm import Session

from app.auth.security import (
    create_access_token,
    create_refresh_token,
    create_user_id,
    hash_password,
    verify_password,
)
from app.models.user import User
from app.schemas.user import UserCreate


class AuthService:
    @staticmethod
    def register_user(db: Session, user_data: UserCreate) -> User:
        existing_user = db.query(User).filter(User.email == user_data.email).first()
        if existing_user:
            return existing_user

        user = User(
            id=create_user_id(),
            email=user_data.email,
            hashed_password=hash_password(user_data.password),
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    @staticmethod
    def authenticate_user(db: Session, email: str, password: str) -> User | None:
        user = db.query(User).filter(User.email == email).first()
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user

    @staticmethod
    def create_token(user: User) -> tuple[str, str]:
        return create_access_token(user.id), create_refresh_token(user.id)
