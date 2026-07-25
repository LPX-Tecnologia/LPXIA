from dataclasses import dataclass
from typing import List


@dataclass
class DocumentChunk:
    id: str
    title: str
    content: str
    embedding: list[float]


class RAGService:
    def __init__(self) -> None:
        self.documents: List[DocumentChunk] = []

    def add_document(self, title: str, content: str) -> DocumentChunk:
        chunk = DocumentChunk(
            id=str(len(self.documents) + 1),
            title=title,
            content=content,
            embedding=self._simple_embedding(content),
        )
        self.documents.append(chunk)
        return chunk

    def search(self, query: str, limit: int = 3) -> List[DocumentChunk]:
        query_embedding = self._simple_embedding(query)
        scored = []
        for document in self.documents:
            score = self._cosine_similarity(query_embedding, document.embedding)
            scored.append((score, document))
        scored.sort(key=lambda item: item[0], reverse=True)
        return [document for _, document in scored[:limit]]

    def _simple_embedding(self, text: str) -> list[float]:
        lowered = text.lower()
        tokens = [token for token in lowered.replace("\n", " ").split(" ") if token]
        vector = []
        for token in sorted(set(tokens)):
            vector.append(lowered.count(token))
        return vector

    def _cosine_similarity(self, left: list[float], right: list[float]) -> float:
        if not left or not right:
            return 0.0
        max_len = max(len(left), len(right))
        left_padded = left + [0.0] * (max_len - len(left))
        right_padded = right + [0.0] * (max_len - len(right))
        numerator = sum(a * b for a, b in zip(left_padded, right_padded))
        denominator = (sum(a * a for a in left_padded) ** 0.5) * (sum(b * b for b in right_padded) ** 0.5)
        if denominator == 0:
            return 0.0
        return numerator / denominator
