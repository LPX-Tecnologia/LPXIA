"""Generation endpoints: text, code, image, video.

Text and code use `app.core.ai_client` (real OpenAI client if OPENAI_API_KEY
is set, otherwise the local stub). Image and video generation require a
dedicated provider (DALL-E, Stability, Runway, etc.) that is not configured
by default — those endpoints return a clear, honest "not configured" status
instead of pretending to generate something.
"""
from fastapi import APIRouter
from pydantic import BaseModel

from app.core import get_ai_client

router = APIRouter()


class GenerateRequest(BaseModel):
    prompt: str


class GenerateResponse(BaseModel):
    status: str
    output: str
    provider: str


CODE_INSTRUCTION = (
    "Voce e um gerador de codigo. Responda APENAS com o codigo solicitado, "
    "em um bloco, sem explicacoes antes ou depois. Pedido do usuario: "
)


@router.post("/text", response_model=GenerateResponse)
async def generate_text(payload: GenerateRequest):
    client = get_ai_client()
    output = await client.complete(payload.prompt)
    provider = "openai" if type(client).__name__ == "OpenAIClient" else "stub-local"
    return GenerateResponse(status="ok", output=output, provider=provider)


@router.post("/code", response_model=GenerateResponse)
async def generate_code(payload: GenerateRequest):
    client = get_ai_client()
    output = await client.complete(CODE_INSTRUCTION + payload.prompt)
    provider = "openai" if type(client).__name__ == "OpenAIClient" else "stub-local"
    return GenerateResponse(status="ok", output=output, provider=provider)


@router.post("/image", response_model=GenerateResponse)
async def generate_image(payload: GenerateRequest):
    return GenerateResponse(
        status="not_configured",
        output=(
            "Geracao de imagem ainda nao tem um provedor configurado. "
            "Adicione uma chave de um servico como OpenAI Images, Stability AI "
            "ou similar e implemente a chamada aqui em app/api/generate.py."
        ),
        provider="none",
    )


@router.post("/video", response_model=GenerateResponse)
async def generate_video(payload: GenerateRequest):
    return GenerateResponse(
        status="not_configured",
        output=(
            "Geracao de video ainda nao tem um provedor configurado. "
            "Servicos como Runway ou Luma tem custo por geracao e precisam "
            "de integracao dedicada em app/api/generate.py."
        ),
        provider="none",
    )
