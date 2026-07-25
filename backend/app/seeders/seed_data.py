from app.database import SessionLocal
from app.models.user import User
from app.auth.security import hash_password


def seed_users() -> None:
    db = SessionLocal()
    try:
        if db.query(User).count() == 0:
            db.add(
                User(
                    id="seed-admin",
                    email="admin@lpxnexus.com",
                    hashed_password=hash_password("admin123"),
                    is_superuser=True,
                )
            )
            db.commit()
    finally:
        db.close()
