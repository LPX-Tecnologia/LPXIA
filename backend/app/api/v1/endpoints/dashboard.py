from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.auth.security import get_current_user
from app.database import get_db
from app.models.user import User

router = APIRouter(prefix="/dashboard", tags=["dashboard"])


@router.get("/summary")
def dashboard_summary(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> dict[str, object]:
    user_count = db.query(User).count()
    return {
        "stats": {
            "users": user_count,
            "projects": 24,
            "active_ai_agents": 9,
            "logs_today": 1842,
        },
        "users": [
            {"id": current_user.id, "name": current_user.email.split("@", 1)[0], "role": "Admin" if current_user.is_superuser else "Operator", "status": "Active"},
            {"id": 2, "name": "Bruno", "role": "Operator", "status": "Active"},
            {"id": 3, "name": "Cris", "role": "Viewer", "status": "Pending"},
        ],
        "projects": [
            {"id": 1, "name": "LPX-NEXUS", "status": "In Progress", "owner": current_user.email.split("@", 1)[0]},
            {"id": 2, "name": "Marketing Copilot", "status": "Review", "owner": "Bruno"},
            {"id": 3, "name": "Ops Agent", "status": "Live", "owner": "Cris"},
        ],
        "ai": [
            {"id": 1, "name": "Research Agent", "health": "Stable"},
            {"id": 2, "name": "Design Agent", "health": "Warning"},
            {"id": 3, "name": "Support Agent", "health": "Stable"},
        ],
        "logs": [
            {"id": 1, "message": "Project deployed successfully", "level": "INFO"},
            {"id": 2, "message": "Agent sync delayed", "level": "WARN"},
            {"id": 3, "message": "Authentication failure", "level": "ERROR"},
        ],
    }
