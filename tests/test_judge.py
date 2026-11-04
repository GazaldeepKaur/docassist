"""Run: python -m tests.test_judge   (plain asserts; no network, no OpenAI)"""
from evals.judge import citation_check, cited_pages, is_abstention, parse_verdict, summarize

# --- abstention detection
assert is_abstention("I don't know based on the provided documents.")
assert is_abstention("I don't know based on the provided documents")           # missing final period
assert not is_abstention("You need a Permanent resident card [welcome.pdf, page 47].")

# --- citations: single, repeated, and the semicolon form the model really produced
assert cited_pages("See [welcome.pdf, page 47].") == [("welcome.pdf", 47)]
assert cited_pages("[apply_SIN.pdf, page 3; welcome.pdf, page 48]") == [("apply_SIN.pdf", 3), ("welcome.pdf", 48)]
assert cited_pages("no citation here") == []
retrieved = [("welcome.pdf", 47), ("apply_SIN.pdf", 3)]
assert citation_check("x [welcome.pdf, page 47]", retrieved)["valid"]
assert not citation_check("x [welcome.pdf, page 99]", retrieved)["valid"]          # page never retrieved
assert citation_check("x [welcome.pdf, page 99]", retrieved)["invalid"] == [("welcome.pdf", 99)]
assert not citation_check("claim without a citation", retrieved)["valid"]

# --- verdict parsing
good = '{"correctness": 2, "grounded": true, "reason": "matches page 3"}'
assert parse_verdict(good) == {"correctness": 2, "grounded": True, "reason": "matches page 3"}
assert parse_verdict("Sure! " + good + " Hope that helps")["correctness"] == 2     # extra words around the JSON
assert parse_verdict('{"correctness": 5, "grounded": true}') is None                # out of range
assert parse_verdict('{"correctness": 1, "grounded": "yes"}') is None               # not a boolean
assert parse_verdict("not json") is None

# --- summary arithmetic on a tiny hand-made set
cit_ok, cit_bad = {"valid": True, "invalid": []}, {"valid": False, "invalid": [("x.pdf", 1)]}
rows = [
    {"id": "a", "answerable": True, "abstained": False, "correctness": 2, "grounded": True, "citations": cit_ok},
    {"id": "b", "answerable": True, "abstained": False, "correctness": 1, "grounded": False, "citations": cit_bad},
    {"id": "c", "answerable": True, "abstained": True, "correctness": 0, "grounded": None, "citations": cit_bad},
    {"id": "d", "answerable": False, "abstained": True, "correctness": None, "grounded": None, "citations": cit_bad},
    {"id": "e", "answerable": False, "abstained": False, "correctness": None, "grounded": True, "citations": cit_ok},
]
s = summarize(rows)
assert s["avg_correctness_0_to_2"] == 1.0            # (2 + 1 + 0) / 3
assert s["fully_correct_pct"] == 33.3                # 1 of 3
assert s["grounded_pct_of_answered"] == 50.0         # a True, b False (c abstained, skipped)
assert s["valid_citations_pct_of_answered"] == 50.0  # a valid, b invalid
assert s["false_abstention_pct"] == 33.3             # c
assert s["abstention_accuracy_pct"] == 50.0          # d yes, e no
print("judge tests passed")
