from typing import List
from uuid import uuid4

from sqlalchemy.orm import Session

from app.memory.models import Memory


class MemoryRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, user_id: str, payload: dict) -> Memory:
        memory = Memory(id=str(uuid4()), user_id=user_id, **payload)
        self.db.add(memory)
        self.db.commit()
        self.db.refresh(memory)
        return memory

    def list_by_user(self, user_id: str) -> List[Memory]:
        return self.db.query(Memory).filter(Memory.user_id == user_id).order_by(Memory.created_at.desc()).all()

    def get(self, memory_id: str, user_id: str) -> Memory | None:
        return self.db.query(Memory).filter(Memory.id == memory_id, Memory.user_id == user_id).first()

    def delete(self, memory_id: str, user_id: str) -> bool:
        memory = self.get(memory_id, user_id)
        if not memory:
            return False
        self.db.delete(memory)
        self.db.commit()
        return True
