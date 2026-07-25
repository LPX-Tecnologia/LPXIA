"""AI client with a safe local stub fallback.

If OPENAI_API_KEY is not set, `get_ai_client()` returns a `StubAIClient`
that never makes network calls and never fails due to quota/billing issues.
Once a real key is configured, it automatically switches to `OpenAIClient`.
The `openai` package is only imported lazily, inside `OpenAIClient`, so it
is not a hard requirement to boot the backend.
"""
from __future__ import annotations

from app.config import get_settings


class StubAIClient:
    """Deterministic, offline stand-in for a real LLM client."""

    def __init__(self, model: str = "local-stub"):
        self.model = model

    async def complete(self, prompt: str) -> str:
        return f"[stub-response model={self.model}] echo: {prompt[:200]}"


class OpenAIClient:
    """Thin wrapper around the official OpenAI SDK."""

    def __init__(self, api_key: str, model: str):
        from openai import OpenAI  # optional dependency, imported only if needed

        self._client = OpenAI(api_key=api_key)
        self.model = model

    async def complete(self, prompt: str) -> str:
        response = self._client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
        )
        return response.choices[0].message.content or ""


def get_ai_client():
    """Returns a real OpenAI client if configured, otherwise a local stub."""
    settings = get_settings()
    if settings.ai_enabled:
        return OpenAIClient(api_key=settings.openai_api_key, model=settings.openai_model)
    return StubAIClient(model=settings.openai_model)
