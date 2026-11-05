# docassist
DocAssist is an assistant that answers newcomer-to-Canada questions from official government guides and cites the exact document and page behind every claim. It behaves like a real RAG product: answers can be checked, wrong answers matter, and "I don't know" is sometimes the correct output.

Status: Day 3 (basic RAG with citations, a 30-question evaluation set, chunk-size experiments and an
LLM judge). Hybrid search, agent and guardrails are added in later days.

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

- [x] `python -m src.ingest` finishes and prints chunk counts for 17 PDFs
- [x] 5 hand-written questions each return an answer with a correct `[file, page]` citation
- [x] An unrelated question ("Who won the hockey game?") returns "I don't know based on the provided documents."

## Evaluation

Test set (`evals/questions.json`): 30 questions: 20 direct, 5 multi-source (the answer is spread over
several pages) and 5 unanswerable. Each answerable question lists its gold pages as (file, page) with an anchor
phrase; `python -m evals.check_questions` verifies every anchor against the PDFs.

```powershell
python -m evals.run_eval --label x --collection docassist_1000_100     # retrieval only, free
python -m evals.judge --label x --collection docassist_1000_100        # answers + LLM judge, a few cents
```

### Retrieval: chunk size (embedding model bge-small-en-v1.5, 10 chunks retrieved per question)

hit@k = a gold page is in the top k. cov@k = share of the needed gold pages found in the top k.
MRR = mean of 1/rank of the first gold page.

| Label (results file) | Chunk size / overlap | hit@1 | hit@5 | hit@10 | MRR | cov@5 |
|---|---|---|---|---|---|---|
| `baseline2` (`baseline2.json`) | 2000 / 200 (baseline) | 0.68 | 0.88 | 0.96 | 0.755 | 0.78 |
| `c1000_100` (`c1000_100.json`) | **1000 / 100 (chosen)** | 0.72 | 0.92 | 0.96 | 0.784 | 0.84 |
| `c500_50` (`c500_50.json`) | 500 / 50 | 0.72 | 0.88 | 0.92 | 0.764 | 0.83 |
| `c1000_0` (`c1000_0.json`) | 1000 / 0 | 0.72 | 0.84 | 0.88 | 0.777 | 0.79 |

- 1000/100 raised hit@5 from 0.88 to 0.92 (one question out of 25) and fixed three of the four single-answer
  misses of the baseline. Without overlap, hit@5 fell to 0.84. 500/50 was worse than 1000/100 at k=10.
- At a similar amount of context (about 10,000 characters), 1000/100 with k=10 reached hit 0.96 and cov 0.90
  against 0.88 and 0.78 for 2000/200 with k=5.
- Multi-source questions stay weak at every size (cov@5 between 0.37 and 0.55).

### Answer quality (settings: 1000/100, k=5, generator gpt-4o-mini, judge gpt-4o)

| Label (results file) | Grading run | Avg correctness (0-2) | Fully correct | Grounded | Valid citations |
|---|---|---|---|---|---|
| `j1_old` (`judge_j1_old.json`) | First generator prompt, first grading | 1.68 | 80.0% | 87.5% | 87.5% |
| `j1` (`judge_j1.json`) | Same answers, judge prompt clarified | 1.68 | 84.0% | 87.5% | 87.5% |
| `j2` (`judge_j2.json`) | Concrete citation instruction in the generator prompt | 1.60 | 76.0% | 83.3% | 100.0% |
| `j2r` (`judge_j2r.json`) | Same answers as `j2`, graded again | 1.60 | 80.0% | 83.3% | 100.0% |

`j1_old` is a copy of the first `j1` grading, saved before the judge prompt was changed and `j1` was re-graded.
Answers are stored in `answers_j1.json` (rows `j1_old` and `j1`) and `answers_j2.json` (rows `j2` and `j2r`).

- Fully correct ranged from 76% to 84% and average correctness from 1.60 to 1.68 across gradings.
  Grounded was 83-88% of non-abstained answers.
- Citation validity rose from 87.5% to 100% after the system prompt gave a concrete example
  (`[welcome.pdf, page 47]`). Before, the model sometimes wrote the literal placeholder `[source, page]`.
- All 5 unanswerable questions were refused in every run; 1 of 25 answerable questions was wrongly refused.
- Questions that fail in every run (q04, q08, q21, q25) trace back to retrieval: the chunk with the key
  sentence was not among the chunks sent to the model.

## Limitations

- **Same vendor.** The answers come from gpt-4o-mini and are graded by gpt-4o. Models from one vendor can share
  blind spots or favour their own style. A judge from another model family would be a better check.
- **Small test set.** 25 answerable and 5 unanswerable questions. One answerable question moves a percentage
  by 4 points and one unanswerable question by 20, so differences under about 8 points are noise. "5 of 5
  refused" could have been 4 of 5 on another set. The questions were written after reading the PDFs, so their
  wording is closer to the documents than real users' questions would be.
- **Noisy grading.** Grading identical answers again changed the grade of 2 of 25 rows each time (q15 and q21;
  q11 and q15). Generation also varies: 5 of 30 answers differed in wording between two runs at temperature 0.
  The ranges above are the honest figures, not any single run.
- **Judge mistakes found by hand.** For q04 the judge marked a supported claim as not grounded because it mixed
  completeness into groundedness; for q11 it marked supported claims as unsupported. `grounded = false` is not
  proof of hallucination: it also covers outside knowledge, over-reading and judge errors.
- **Page-level retrieval scoring is generous.** A retrieval counts as a hit when the gold page is found, even
  if the retrieved chunk lacks the key sentence (q04, q11). Chunk-level scoring is the next improvement.
- The judge reads only the retrieved context and the gold pages. English documents only, from one snapshot date.

## Sources

Add the URL each PDF was downloaded from here (needed for the final README).
