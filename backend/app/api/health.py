"""Health check endpoints."""
from fastapi import APIRouter, Request

from app.config import get_settings
from app.utils import utc_now_iso

router = APIRouter()


@router.get("")
async def health_check(request: Request):
    """Basic liveness check used by uptime monitors and Docker healthchecks."""
    settings = get_settings()
    return {
        "status": "ok",
        "app": settings.app_name,
        "version": settings.app_version,
        "environment": settings.app_env,
        "ai_enabled": getattr(request.app.state, "ai_enabled", settings.ai_enabled),
        "timestamp": utc_now_iso(),
    }


@router.get("/ready")
async def readiness_check():
    """Readiness probe (extend with DB/cache checks as they're added)."""
    return {"status": "ready"}
