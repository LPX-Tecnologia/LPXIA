from fastapi import APIRouter
from pydantic import BaseModel

from app.rag.service import RAGService

router = APIRouter(prefix="/rag", tags=["rag"])

service = RAGService()


class DocumentInput(BaseModel):
    title: str
    content: str


class SearchQuery(BaseModel):
    query: str
    limit: int = 3


class RetrievedDocument(BaseModel):
    id: str
    title: str
    content: str


@router.post("/documents", response_model=RetrievedDocument)
def add_document(payload: DocumentInput) -> RetrievedDocument:
    document = service.add_document(payload.title, payload.content)
    return RetrievedDocument(id=document.id, title=document.title, content=document.content)


@router.post("/search", response_model=list[RetrievedDocument])
def search_documents(payload: SearchQuery) -> list[RetrievedDocument]:
    documents = service.search(payload.query, limit=payload.limit)
    return [RetrievedDocument(id=document.id, title=document.title, content=document.content) for document in documents]
