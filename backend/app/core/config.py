import os
from functools import lru_cache
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "LPX-NEXUS"
    app_version: str = "0.1.0"
    api_v1_prefix: str = "/api/v1"
    database_url: str = os.getenv("DATABASE_URL", "sqlite:///./lpxnexus.db")
    redis_url: str = os.getenv("REDIS_URL", "redis://localhost:6379/0")
    jwt_secret_key: str = os.getenv("JWT_SECRET_KEY", "dev-secret-key")
    jwt_algorithm: str = os.getenv("JWT_ALGORITHM", "HS256")
    access_token_expire_minutes: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "60"))
    env: str = os.getenv("ENV", "development")
    log_level: str = os.getenv("LOG_LEVEL", "INFO")

    class Config:
        env_file = ".env"
        case_sensitive = False


@lru_cache()
def get_settings() -> Settings:
    return Settings()
