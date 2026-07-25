from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.auth.security import get_current_user
from app.database import get_db
from app.memory.schemas import MemoryCreate, MemoryOut
from app.memory.service import MemoryService
from app.models.user import User

router = APIRouter(prefix="/memory", tags=["memory"])

VALID_MEMORY_TYPES = {"short_term", "long_term", "preferences", "feedback", "preference"}


def normalize_memory_type(memory_type: str) -> str:
    if memory_type == "preference":
        return "preferences"
    return memory_type


@router.post("/", response_model=MemoryOut, status_code=status.HTTP_201_CREATED)
def create_memory(payload: MemoryCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)) -> MemoryOut:
    if payload.memory_type not in VALID_MEMORY_TYPES:
        raise HTTPException(status_code=400, detail="Invalid memory type")
    payload.memory_type = normalize_memory_type(payload.memory_type)
    service = MemoryService(db)
    return service.add_memory(current_user, payload)


@router.get("/", response_model=list[MemoryOut])
def list_memories(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)) -> list[MemoryOut]:
    service = MemoryService(db)
    return service.list_memories(current_user)


@router.delete("/{memory_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_memory(memory_id: str, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)) -> None:
    service = MemoryService(db)
    if not service.delete_memory(current_user, memory_id):
        raise HTTPException(status_code=404, detail="Memory not found")
