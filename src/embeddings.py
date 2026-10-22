"""Turn text into vectors with a local sentence-transformers model."""
from functools import lru_cache

from sentence_transformers import SentenceTransformer

from .config import EMBED_MODEL

# bge models work best when the *question* (not the passages) gets this prefix.
QUERY_PREFIX = "Represent this sentence for searching relevant passages: "


@lru_cache(maxsize=1)
def get_model() -> SentenceTransformer:
    return SentenceTransformer(EMBED_MODEL)


def embedding_dim() -> int:
    return len(get_model().encode("dimension probe"))


def embed_passages(texts: list[str], batch_size: int = 32) -> list[list[float]]:
    model = get_model()
    vectors = model.encode(
        texts, batch_size=batch_size, normalize_embeddings=True, show_progress_bar=False
    )
    # lengths = [len(model.tokenizer(t)["input_ids"]) for t in texts]
    # over = sum(n > model.max_seq_length for n in lengths)
    # print(f"    tokens: max {max(lengths)}, over {model.max_seq_length}: {over}/{len(lengths)}")
    return vectors.tolist()


def embed_query(question: str) -> list[float]:
    prefix = QUERY_PREFIX if "bge" in EMBED_MODEL.lower() else ""
    vector = get_model().encode(prefix + question, normalize_embeddings=True)
    return vector.tolist()
