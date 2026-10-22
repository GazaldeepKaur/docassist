"""Run: python -m tests.test_metrics   (plain asserts, no pytest needed)"""
from evals.metrics import coverage_at_k, first_hit_rank, hit_at_k, reciprocal_rank

A, B, C, D = ("a.pdf", 1), ("b.pdf", 2), ("c.pdf", 3), ("d.pdf", 4)

assert first_hit_rank([A, B, C], {C}) == 3
assert first_hit_rank([A, B], {C}) is None
assert hit_at_k([A, B, C], {C}, 2) == 0.0
assert hit_at_k([A, B, C], {C}, 3) == 1.0
assert hit_at_k([A, B, C], {B, C}, 2) == 1.0          # any gold page counts
assert coverage_at_k([A, B, C], {B, C, D}, 3) == 2 / 3
assert coverage_at_k([A, B, C], {B, C, D}, 1) == 0.0
assert reciprocal_rank([A, B, C], {A}) == 1.0
assert reciprocal_rank([A, B, C], {B, C}) == 0.5      # first gold hit decides
assert reciprocal_rank([A, B, C], {D}) == 0.0
try:
    coverage_at_k([A], set(), 1)
except ValueError:
    pass
else:
    raise AssertionError("empty gold must raise")
print("metrics tests passed")
