## 2026-07-08 - Pandas Loop Filtering Memory Leak
**Learning:** Sequential DataFrame filtering (`df = df[...]`) within loops causes expensive O(N) memory allocations per iteration in pandas data processing scripts.
**Action:** Use a cumulative boolean mask (`mask &= ...`) and filter once at the end. Use `df.loc[mask, col]` to compute on the active subset, and `mask.sum()` to count active rows dynamically.
