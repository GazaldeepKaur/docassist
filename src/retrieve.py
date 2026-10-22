"""Find the chunks most similar to a question."""
from dataclasses import dataclass
from functools import lru_cache

from qdrant_client import QdrantClient

from . import config
from .embeddings import embed_query


@dataclass
class Hit:
    source: str
    page: int
    text: str
    score: float


@lru_cache(maxsize=1)
def get_client() -> QdrantClient:
    return QdrantClient(url=config.QDRANT_URL)


def retrieve(question: str, top_k: int = config.TOP_K) -> list[Hit]:
    result = get_client().query_points(
        collection_name=config.COLLECTION,
        query=embed_query(question),
        limit=top_k,
        with_payload=True,
    )
    return [
        Hit(
            source=p.payload["source"],
            page=p.payload["page"],
            text=p.payload["text"],
            score=float(p.score),
        )
        for p in result.points
    ]
