from app.auth.security import get_current_user
from app.memory.repository import MemoryRepository
from app.memory.schemas import MemoryCreate, MemoryOut
from app.models.user import User
from sqlalchemy.orm import Session


class MemoryService:
    def __init__(self, db: Session):
        self.db = db
        self.repository = MemoryRepository(db)

    def add_memory(self, user: User, payload: MemoryCreate) -> MemoryOut:
        memory = self.repository.create(
            user_id=user.id,
            payload={
                "title": payload.title,
                "content": payload.content,
                "memory_type": payload.memory_type,
            },
        )
        return MemoryOut(**memory.__dict__)

    def list_memories(self, user: User) -> list[MemoryOut]:
        memories = self.repository.list_by_user(user.id)
        return [MemoryOut(**memory.__dict__) for memory in memories]

    def delete_memory(self, user: User, memory_id: str) -> bool:
        return self.repository.delete(memory_id, user.id)
