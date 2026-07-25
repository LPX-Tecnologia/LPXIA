from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/chat", tags=["chat"])


class ChatMessage(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    session_id: str | None = None
    message: str


class ChatResponse(BaseModel):
    session_id: str
    reply: str
    history: list[ChatMessage]


sessions: dict[str, list[ChatMessage]] = {}


@router.post("/send", response_model=ChatResponse)
def send_message(payload: ChatRequest) -> ChatResponse:
    session_id = payload.session_id or "default"
    history = sessions.setdefault(session_id, [])

    history.append(ChatMessage(role="user", content=payload.message))
    reply = f"Echo: {payload.message}"
    history.append(ChatMessage(role="assistant", content=reply))

    return ChatResponse(session_id=session_id, reply=reply, history=history)


@router.get("/sessions")
def list_sessions() -> dict[str, list[dict[str, str]]]:
    return {session_id: [message.model_dump() for message in history] for session_id, history in sessions.items()}


@router.get("/sessions/{session_id}")
def get_session(session_id: str) -> list[dict[str, str]]:
    return [message.model_dump() for message in sessions.get(session_id, [])]
