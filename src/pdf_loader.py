"""Read a PDF page by page. The page number is kept so every answer can cite it."""
from pathlib import Path
from typing import Iterator

from pypdf import PdfReader


def extract_pages(pdf_path: Path) -> Iterator[tuple[int, str]]:
    """Yield (page_number, text) with page numbers starting at 1. Unreadable pages are skipped."""
    reader = PdfReader(str(pdf_path))
    for number, page in enumerate(reader.pages, start=1):
        try:
            text = page.extract_text() or ""
        except Exception as exc:  # one broken page should not stop the whole ingest
            print(f"  ! {pdf_path.name} page {number}: {exc}")
            continue
        yield number, text
