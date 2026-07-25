from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/orchestrator", tags=["orchestrator"])


class OrchestratorRequest(BaseModel):
    agent: str
    prompt: str
    context: str | None = None
    use_memory: bool = True
    tools: list[str] | None = None


class ToolPlan(BaseModel):
    name: str
    purpose: str


class OrchestratorResponse(BaseModel):
    agent: str
    summary: str
    context: str | None
    memory_used: bool
    tools: list[ToolPlan]


AGENT_PROFILES = {
    "research": {
        "name": "Research Agent",
        "description": "Handles synthesis, analysis, and market context.",
        "tools": ["web_search", "summarize", "memory_lookup"],
    },
    "design": {
        "name": "Design Agent",
        "description": "Supports UX ideas, interface directions, and copy.",
        "tools": ["design_system", "memory_lookup"],
    },
    "ops": {
        "name": "Ops Agent",
        "description": "Coordinates workflows, deploys, and operational checks.",
        "tools": ["deploy", "logs", "memory_lookup"],
    },
}


@router.post("/plan", response_model=OrchestratorResponse)
def plan_execution(payload: OrchestratorRequest) -> OrchestratorResponse:
    profile = AGENT_PROFILES.get(payload.agent, AGENT_PROFILES["research"])
    tools = [ToolPlan(name=tool, purpose=f"Supports {profile['name']}") for tool in profile["tools"]]

    if payload.tools:
        selected = [tool for tool in tools if tool.name in payload.tools]
        tools = selected or tools

    summary = (
        f"{profile['name']} selected for request: {payload.prompt}. "
        f"Context: {payload.context or 'none'}."
    )

    return OrchestratorResponse(
        agent=profile["name"],
        summary=summary,
        context=payload.context,
        memory_used=payload.use_memory,
        tools=tools,
    )
