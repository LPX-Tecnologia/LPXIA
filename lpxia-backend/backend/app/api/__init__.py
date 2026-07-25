"""Aggregates all API routers into a single api_router."""
from fastapi import APIRouter

from app.api.health import router as health_router
from app.api.generate import router as generate_router

api_router = APIRouter()
api_router.include_router(health_router, prefix="/health", tags=["health"])
api_router.include_router(generate_router, prefix="/generate", tags=["generate"])
