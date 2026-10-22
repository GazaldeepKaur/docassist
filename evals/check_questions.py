"""Check that every gold (file, page) really contains its anchor text.

    python -m evals.check_questions

Run it after editing evals/questions.json and whenever PDFs change.
"""
import json
import re
import sys
from pathlib import Path

from src import config
from src.chunking import normalize
from src.pdf_loader import extract_pages

QUESTIONS = Path(__file__).with_name("questions.json")


def main() -> int:
    questions = json.loads(QUESTIONS.read_text(encoding="utf-8"))
    cache: dict[str, dict[int, str]] = {}
    problems = 0

    for q in questions:
        for g in q["gold"]:
            src = g["source"]
            if src not in cache:
                path = config.DATA_DIR / src
                if not path.exists():
                    cache[src] = {}
                    print(f"[{q['id']}] MISSING FILE {path}")
                    problems += 1
                else:
                    cache[src] = {n: normalize(t) for n, t in extract_pages(path)}
            text = cache[src].get(g["page"], "")
            if not re.search(re.escape(g["anchor"]), text, re.IGNORECASE):
                print(f"[{q['id']}] anchor {g['anchor']!r} NOT on {src} p{g['page']}")
                problems += 1

    kinds: dict[str, int] = {}
    for q in questions:
        kinds[q["type"]] = kinds.get(q["type"], 0) + 1
    print(f"{len(questions)} questions {kinds}; {problems} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
