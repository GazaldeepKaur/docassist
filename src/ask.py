"""Ask a question from the command line, without starting the API:
    python -m src.ask "Who can apply for a Social Insurance Number?"
    python -m src.ask --retrieval-only "How do I protect my SIN?"
"""
import argparse
import sys

from . import config
from .retrieve import retrieve


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")  # Windows consoles choke on some PDF characters
    parser = argparse.ArgumentParser()
    parser.add_argument("question")
    parser.add_argument("--top-k", type=int, default=config.TOP_K)
    parser.add_argument("--retrieval-only", action="store_true", help="show the retrieved chunks, skip the LLM")
    args = parser.parse_args()

    hits = retrieve(args.question, args.top_k)
    if not args.retrieval_only:
        from .generate import generate_answer
        print("\nANSWER\n" + generate_answer(args.question, hits))

    print("\nRETRIEVED")
    for i, h in enumerate(hits, start=1):
        print(f"{i}. {h.source}, page {h.page}  (score {h.score:.3f})")
        print("   " + h.text[:200].replace("\n", " ") + "...")


if __name__ == "__main__":
    main()
