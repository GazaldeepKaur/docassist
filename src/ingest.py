"""Build the index: read PDFs, chunk each page, embed the chunks, store them in Qdrant.

Run from the project folder:
    python -m src.ingest
    python -m src.ingest --chunk-size 1000 --chunk-overlap 100     (Day 3 experiments)
"""
import argparse
import time
from pathlib import Path

from qdrant_client import QdrantClient
from qdrant_client.models import Distance, PointStruct, VectorParams

from . import config
from .chunking import chunk_text
from .embeddings import embed_passages, embedding_dim
from .pdf_loader import extract_pages

MIN_PAGE_CHARS = 50   # skip near-empty pages (cover pages, page-number-only pages)
BATCH = 64            # chunks embedded and uploaded per step


def main() -> None:
    parser = argparse.ArgumentParser(description="Index PDFs into Qdrant")
    parser.add_argument("--data-dir", type=Path, default=config.DATA_DIR)
    parser.add_argument("--chunk-size", type=int, default=config.CHUNK_SIZE)
    parser.add_argument("--chunk-overlap", type=int, default=config.CHUNK_OVERLAP)
    parser.add_argument("--keep", action="store_true", help="add to the existing collection instead of rebuilding it")
    args = parser.parse_args()

    pdfs = sorted(args.data_dir.glob("*.pdf"), key=lambda p: p.name.lower())
    if not pdfs:
        raise SystemExit(f"No PDF files found in {args.data_dir}")
    print(f"{len(pdfs)} PDFs in {args.data_dir}  |  chunk size {args.chunk_size}, overlap {args.chunk_overlap}")

    client = QdrantClient(url=config.QDRANT_URL)
    next_id = 0
    if args.keep and client.collection_exists(config.COLLECTION):
        next_id = client.count(config.COLLECTION, exact=True).count
    else:
        if client.collection_exists(config.COLLECTION):
            client.delete_collection(config.COLLECTION)
        client.create_collection(
            collection_name=config.COLLECTION,
            vectors_config=VectorParams(size=embedding_dim(), distance=Distance.COSINE),
        )

    total_chunks = 0
    started = time.time()
    for pdf in pdfs:
        t0 = time.time()
        records: list[dict] = []
        pages = 0
        for page_number, text in extract_pages(pdf):
            pages += 1
            if len(text.strip()) < MIN_PAGE_CHARS:
                continue
            for index, piece in enumerate(chunk_text(text, args.chunk_size, args.chunk_overlap)):
                records.append({"source": pdf.name, "page": page_number, "chunk": index, "text": piece})

        for i in range(0, len(records), BATCH):
            batch = records[i:i + BATCH]
            vectors = embed_passages([r["text"] for r in batch])
            client.upsert(
                collection_name=config.COLLECTION,
                points=[
                    PointStruct(id=next_id + j, vector=vec, payload=rec)
                    for j, (vec, rec) in enumerate(zip(vectors, batch))
                ],
            )
            next_id += len(batch)

        total_chunks += len(records)
        print(f"  {pdf.name:55} {pages:4} pages -> {len(records):5} chunks  ({time.time() - t0:5.1f}s)")

    stored = client.count(config.COLLECTION, exact=True).count
    print(f"Done: {total_chunks} chunks indexed, {stored} points in '{config.COLLECTION}', {time.time() - started:.0f}s total")


if __name__ == "__main__":
    main()
