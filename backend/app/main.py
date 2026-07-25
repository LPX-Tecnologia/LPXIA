from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.endpoints.auth import router as auth_router
from app.api.v1.endpoints.chat import router as chat_router
from app.api.v1.endpoints.dashboard import router as dashboard_router
from app.api.v1.endpoints.health import router as health_router
from app.api.v1.endpoints.memory import router as memory_router
from app.api.v1.endpoints.modules import router as modules_router
from app.api.v1.endpoints.orchestrator import router as orchestrator_router
from app.api.v1.endpoints.rag import router as rag_router
from app.core.config import get_settings
from app.core.logging import configure_logging
from app.database import Base, engine
from app.initial_data import create_initial_user
from app.middleware.request_logging import RequestLoggingMiddleware

settings = get_settings()
configure_logging()

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(RequestLoggingMiddleware)

app.include_router(auth_router, prefix=settings.api_v1_prefix)
app.include_router(memory_router, prefix=settings.api_v1_prefix)
app.include_router(dashboard_router, prefix=settings.api_v1_prefix)
app.include_router(health_router)
app.include_router(chat_router, prefix=settings.api_v1_prefix)
app.include_router(orchestrator_router, prefix=settings.api_v1_prefix)
app.include_router(rag_router, prefix=settings.api_v1_prefix)
app.include_router(modules_router, prefix=settings.api_v1_prefix)


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "LPX-NEXUS backend is running", "status": "ok"}


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "healthy"}


@app.on_event("startup")
def startup() -> None:
    Base.metadata.create_all(bind=engine)
    create_initial_user()
