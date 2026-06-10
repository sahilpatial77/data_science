## 2026-06-10 - Outlier Removal Optimization
**Learning:** Sequential DataFrame filtering inside loops causes O(N) memory allocations per column. Evaluating boolean masks cumulatively and computing quantiles on progressively masked data optimizes performance and memory.
**Action:** Always prefer cumulative mask updates over sequential DataFrame reassignment for filtering operations.
