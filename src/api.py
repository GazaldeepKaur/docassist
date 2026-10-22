"""FastAPI service. Run from the project folder:
    uvicorn src.api:app --reload
then open http://127.0.0.1:8000/docs
"""
import time
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from . import config
from .embeddings import get_model
from .generate import generate_answer
from .retrieve import retrieve


@asynccontextmanager
async def lifespan(app: FastAPI):
    get_model()  # load the embedding model once at startup, not on the first request
    yield


app = FastAPI(title="DocAssist", version="0.1.0", lifespan=lifespan)


class AskRequest(BaseModel):
    question: str = Field(min_length=3, max_length=1000)
    top_k: int = Field(default=config.TOP_K, ge=1, le=20)


class Source(BaseModel):
    source: str
    page: int
    score: float
    snippet: str


class AskResponse(BaseModel):
    answer: str
    sources: list[Source]
    timings_ms: dict[str, int]


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "collection": config.COLLECTION, "llm": config.OPENAI_MODEL}


@app.post("/ask", response_model=AskResponse)
def ask(req: AskRequest) -> AskResponse:
    t0 = time.perf_counter()
    try:
        hits = retrieve(req.question, req.top_k)
    except Exception as exc:
        raise HTTPException(
            status_code=503,
            detail=f"Search failed ({type(exc).__name__}). Is Qdrant running (docker compose up -d) "
                   f"and has `python -m src.ingest` been run? {str(exc)[:200]}",
        )
    t1 = time.perf_counter()

    try:
        answer = generate_answer(req.question, hits)
    except RuntimeError as exc:  # missing API key
        raise HTTPException(status_code=500, detail=str(exc))
    except Exception as exc:
        raise HTTPException(status_code=502, detail=f"LLM call failed ({type(exc).__name__}): {str(exc)[:200]}")
    t2 = time.perf_counter()

    return AskResponse(
        answer=answer,
        sources=[
            Source(source=h.source, page=h.page, score=round(h.score, 4), snippet=h.text[:240])
            for h in hits
        ],
        timings_ms={
            "retrieval": int((t1 - t0) * 1000),
            "generation": int((t2 - t1) * 1000),
            "total": int((t2 - t0) * 1000),
        },
    )
