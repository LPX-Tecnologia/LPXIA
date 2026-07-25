from pydantic import BaseModel


class MemoryCreate(BaseModel):
    title: str
    content: str
    memory_type: str = "short_term"


class MemoryOut(BaseModel):
    id: str
    user_id: str
    title: str
    content: str
    memory_type: str

    class Config:
        from_attributes = True
