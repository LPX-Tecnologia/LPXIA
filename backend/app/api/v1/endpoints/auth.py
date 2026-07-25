from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.auth.security import decode_token, get_current_user, require_admin_user
from app.database import get_db
from app.models.user import User
from app.schemas.user import RefreshTokenRequest, Token, UserCreate, UserLogin, UserOut
from app.services.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def register_user(payload: UserCreate, db: Session = Depends(get_db)) -> User:
    try:
        return AuthService.register_user(db, payload)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@router.post("/login", response_model=Token)
def login(payload: UserLogin, db: Session = Depends(get_db)) -> Token:
    user = AuthService.authenticate_user(db, payload.email, payload.password)
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect email or password")
    access_token, refresh_token = AuthService.create_token(user)
    return Token(access_token=access_token, refresh_token=refresh_token)


@router.post("/refresh", response_model=Token)
def refresh_token(payload: RefreshTokenRequest, db: Session = Depends(get_db)) -> Token:
    try:
        decoded = decode_token(payload.refresh_token)
    except Exception as exc:
        raise HTTPException(status_code=401, detail="Invalid refresh token") from exc

    if decoded.get("type") != "refresh":
        raise HTTPException(status_code=401, detail="Invalid refresh token")

    user = db.query(User).filter(User.id == decoded.get("sub")).first()
    if not user or not user.is_active:
        raise HTTPException(status_code=401, detail="User not found or inactive")

    access_token, refresh_token = AuthService.create_token(user)
    return Token(access_token=access_token, refresh_token=refresh_token)


@router.get("/me", response_model=UserOut)
def get_me(current_user: User = Depends(get_current_user)) -> User:
    return current_user


@router.get("/admin")
def admin_only(current_user: User = Depends(require_admin_user)) -> dict[str, str]:
    return {"message": f"Admin access granted for {current_user.email}"}
