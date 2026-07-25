"""Application startup/shutdown lifecycle."""
import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.config import get_settings

logger = logging.getLogger("lpxia")


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Runs on startup (before yield) and shutdown (after yield)."""
    settings = get_settings()
    logging.basicConfig(level=settings.log_level)

    app.state.settings = settings
    app.state.ai_enabled = settings.ai_enabled

    if settings.ai_enabled:
        logger.info("OpenAI API key detected - real AI client will be used.")
    else:
        logger.warning(
            "OPENAI_API_KEY not set - running with the local AI stub client "
            "(no external calls, no quota required)."
        )

    logger.info(
        "%s v%s starting up in '%s' mode",
        settings.app_name,
        settings.app_version,
        settings.app_env,
    )

    yield

    logger.info("%s shutting down", settings.app_name)
