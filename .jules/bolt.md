## 2026-05-07 - Avoid O(N) DataFrame Memory Allocations in Sequential Filtering
**Learning:** Sequential DataFrame filtering in loops causes O(N) DataFrame memory allocations per iteration.
**Action:** Evaluate boolean masks cumulatively and compute statistics on progressively masked data (e.g., `df.loc[mask, col]`) to avoid reallocation while preserving mathematical behavior.
