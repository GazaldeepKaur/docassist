"""Central settings. Every value can be overridden in the .env file or the environment."""
import os
from pathlib import Path

from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent.parent
load_dotenv(ROOT / ".env")

DATA_DIR = Path(os.getenv("DATA_DIR", ROOT / "data" / "raw"))

QDRANT_URL = os.getenv("QDRANT_URL", "http://localhost:6333")
COLLECTION = os.getenv("QDRANT_COLLECTION", "docassist")

# bge-small-en-v1.5: free, runs on CPU, 384 dimensions.
# Note: it reads at most 512 tokens (roughly 2000 characters). Longer chunks are
# silently truncated before embedding, which matters for the Day 3 chunk-size tests.
EMBED_MODEL = os.getenv("EMBED_MODEL", "BAAI/bge-small-en-v1.5")

CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", "2000"))      # characters
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", "200"))  # characters
TOP_K = int(os.getenv("TOP_K", "5"))

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

NO_ANSWER = "I don't know based on the provided documents."
