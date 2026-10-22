"""Score retrieval against evals/questions.json.

    python -m evals.run_eval --label baseline
    python -m evals.run_eval --label chunk1000 --k 10

Needs Qdrant running and the index built (python -m src.ingest). Does not call OpenAI.
Writes results/<label>.json so later experiments can be compared with this baseline.
"""
import argparse
import json
import sys
from datetime import datetime
from pathlib import Path

from src import config
from src.retrieve import retrieve

from .metrics import coverage_at_k, first_hit_rank, hit_at_k, reciprocal_rank

HERE = Path(__file__).parent
CUTOFFS = (1, 3, 5, 10)


def mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def score_question(q: dict, retrieved: list[tuple]) -> dict:
    gold = {(g["source"], g["page"]) for g in q["gold"]}
    return {
        "first_hit_rank": first_hit_rank(retrieved, gold),
        "rr": reciprocal_rank(retrieved, gold),
        **{f"hit@{k}": hit_at_k(retrieved, gold, k) for k in CUTOFFS},
        **{f"cov@{k}": coverage_at_k(retrieved, gold, k) for k in CUTOFFS},
    }


def summarize(rows: list[dict]) -> dict:
    """Aggregate per-question scores. Unanswerable questions have no gold and are left out."""
    out = {"n": len(rows), "mrr": round(mean([r["rr"] for r in rows]), 3)}
    for k in CUTOFFS:
        out[f"hit@{k}"] = round(mean([r[f"hit@{k}"] for r in rows]), 3)
        out[f"cov@{k}"] = round(mean([r[f"cov@{k}"] for r in rows]), 3)
    return out


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser()
    parser.add_argument("--label", default="baseline", help="name of the results file")
    parser.add_argument("--k", type=int, default=max(CUTOFFS), help="how many chunks to retrieve per question")
    args = parser.parse_args()

    questions = json.loads((HERE / "questions.json").read_text(encoding="utf-8"))
    per_question, answerable, unanswerable = [], [], []

    for q in questions:
        hits = retrieve(q["question"], top_k=args.k)
        retrieved = [(h.source, h.page) for h in hits]
        entry = {
            "id": q["id"], "type": q["type"], "question": q["question"],
            "top_score": round(hits[0].score, 4) if hits else None,
            "retrieved": [{"source": h.source, "page": h.page, "score": round(h.score, 4)} for h in hits],
        }
        if q["gold"]:
            entry.update(score_question(q, retrieved))
            answerable.append(entry)
        else:
            unanswerable.append(entry)
        per_question.append(entry)

    summary = {
        "all_answerable": summarize(answerable),
        "direct": summarize([r for r in answerable if r["type"] == "direct"]),
        "multi": summarize([r for r in answerable if r["type"] == "multi"]),
        "unanswerable_top_scores": [r["top_score"] for r in unanswerable],
        "answerable_top_score_mean": round(mean([r["top_score"] for r in answerable]), 4),
    }
    result = {
        "label": args.label,
        "time": datetime.now().isoformat(timespec="seconds"),
        "settings": {"embed_model": config.EMBED_MODEL, "chunk_size": config.CHUNK_SIZE,
                     "chunk_overlap": config.CHUNK_OVERLAP, "k": args.k},
        "summary": summary,
        "questions": per_question,
    }

    out_dir = config.ROOT / "results"
    out_dir.mkdir(exist_ok=True)
    out_path = out_dir / f"{args.label}.json"
    out_path.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"\n== {args.label} ==")
    for name in ("direct", "multi", "all_answerable"):
        s = summary[name]
        print(f"{name:15} n={s['n']:2}  MRR={s['mrr']:.3f}  "
              + "  ".join(f"hit@{k}={s[f'hit@{k}']:.2f}" for k in CUTOFFS)
              + "   " + "  ".join(f"cov@{k}={s[f'cov@{k}']:.2f}" for k in (5, 10)))
    print(f"top score: answerable mean {summary['answerable_top_score_mean']}, "
          f"unanswerable {summary['unanswerable_top_scores']}")

    print("\nMisses at k=5 (no gold page in the top 5):")
    misses = [r for r in answerable if r["hit@5"] == 0.0]
    for r in misses:
        top = r["retrieved"][0]
        print(f"  {r['id']} {r['question']}\n      top-1 was {top['source']} p{top['page']} ({top['score']})")
    if not misses:
        print("  none")
    print(f"\nSaved {out_path}")


if __name__ == "__main__":
    main()
