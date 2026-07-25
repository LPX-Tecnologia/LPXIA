from sqlalchemy import Column, DateTime, String, Text
from sqlalchemy.sql import func

from app.database import Base


class Memory(Base):
    __tablename__ = "memories"

    id = Column(String, primary_key=True, index=True)
    user_id = Column(String, nullable=False, index=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    memory_type = Column(String, default="fact", nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
