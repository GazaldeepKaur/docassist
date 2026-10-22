"""Split text into overlapping chunks. Pure Python, no third-party imports."""
import re


def normalize(text: str) -> str:
    """Collapse all whitespace (PDF line breaks, double spaces) into single spaces."""
    return re.sub(r"\s+", " ", text).strip()


def chunk_text(text: str, size: int = 2000, overlap: int = 200) -> list[str]:
    """Cut `text` into chunks of about `size` characters that share `overlap` characters.

    Cuts land on a space where possible so words are not split in half.
    """
    if size <= 0:
        raise ValueError("size must be positive")
    if not 0 <= overlap < size // 2:
        raise ValueError("overlap must be at least 0 and less than half of size")

    text = normalize(text)
    n = len(text)
    chunks: list[str] = []
    start = 0
    while start < n:
        end = min(start + size, n)
        if end < n:
            cut = text.rfind(" ", start + size // 2, end)
            if cut != -1:
                end = cut
        piece = text[start:end].strip()
        if piece:
            chunks.append(piece)
        if end >= n:
            break
        next_start = end - overlap
        space = text.find(" ", next_start, end)
        if space != -1:
            next_start = space + 1
        start = max(next_start, start + 1)  # always move forward
    return chunks
