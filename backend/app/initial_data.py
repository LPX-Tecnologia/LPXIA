from app.database import SessionLocal
from app.models.user import User
from app.auth.security import hash_password


def create_initial_user() -> None:
    db = SessionLocal()
    try:
        existing = db.query(User).filter(User.email == "admin@lpxnexus.com").first()
        if not existing:
            user = User(id="admin-user", email="admin@lpxnexus.com", hashed_password=hash_password("admin123"), is_superuser=True)
            db.add(user)
            db.commit()
    finally:
        db.close()
