"""Retrieval metrics. Pure Python, no third-party imports.

A "gold" set is the set of (source, page) pairs that contain the answer.
`retrieved` is the ranked list of (source, page) pairs the retriever returned (best first).
"""


def first_hit_rank(retrieved: list[tuple], gold: set[tuple]) -> int | None:
    """1-based rank of the first retrieved item that is in gold, or None."""
    for i, item in enumerate(retrieved, start=1):
        if item in gold:
            return i
    return None


def hit_at_k(retrieved: list[tuple], gold: set[tuple], k: int) -> float:
    """1.0 if ANY gold page is in the top k, else 0.0 (this is 'recall@k' for single-answer questions)."""
    return 1.0 if any(item in gold for item in retrieved[:k]) else 0.0


def coverage_at_k(retrieved: list[tuple], gold: set[tuple], k: int) -> float:
    """Fraction of the gold pages that appear in the top k (matters for multi-source questions)."""
    if not gold:
        raise ValueError("coverage needs a non-empty gold set")
    return len(gold & set(retrieved[:k])) / len(gold)


def reciprocal_rank(retrieved: list[tuple], gold: set[tuple]) -> float:
    """1/rank of the first gold hit; 0.0 if there is none. The mean over questions is MRR."""
    rank = first_hit_rank(retrieved, gold)
    return 0.0 if rank is None else 1.0 / rank
