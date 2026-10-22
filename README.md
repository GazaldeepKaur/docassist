# docassist
DocAssist is an assistant that answers newcomer-to-Canada questions from official government guides and cites the exact document and page behind every claim. It behaves like a real RAG product: answers can be checked, wrong answers matter, and "I don't know" is sometimes the correct output.

Status: Day 1 (basic RAG with citations). Evaluation, hybrid search, agent and guardrails
are added in later days.

## Run it (Windows PowerShell, from this folder)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt

copy .env.example .env          # then open .env and paste your OPENAI_API_KEY

docker compose up -d            # starts Qdrant on port 6333
python -m src.ingest            # reads data\raw\*.pdf, builds the index (first run downloads the embedding model)
uvicorn src.api:app --reload    # then open http://127.0.0.1:8000/docs
```

Quick check without the API:

```powershell
python -m src.ask "Who can apply for a Social Insurance Number?"
python -m src.ask --retrieval-only "How do I protect my SIN?"
```

## Layout

```
data/raw/        the PDFs that get indexed
data/excluded/   PDFs set aside on purpose (off-topic, duplicates, wrong language)
src/
  config.py      settings (.env)
  pdf_loader.py  PDF -> (page number, text)
  chunking.py    text -> overlapping chunks
  embeddings.py  chunks -> vectors (bge-small-en-v1.5, local)
  ingest.py      builds the Qdrant index
  retrieve.py    question -> top-k chunks
  generate.py    chunks + question -> cited answer (OpenAI)
  api.py         FastAPI: GET /health, POST /ask
  ask.py         command-line version of /ask
```

## Day 1 done-when checklist

- [ ] `python -m src.ingest` finishes and prints chunk counts for 17 PDFs
- [ ] 5 hand-written questions each return an answer with a correct `[file, page]` citation
- [ ] An unrelated question ("Who won the hockey game?") returns "I don't know based on the provided documents."

## Sources

Add the URL each PDF was downloaded from here (needed for the final README).
