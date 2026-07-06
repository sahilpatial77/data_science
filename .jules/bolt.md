## 2026-07-06 - Sequential DataFrame filtering in loops causes O(N) memory allocations
**Learning:** Sequential DataFrame filtering (`df = df[...]`) within loops causes expensive O(N) memory allocations.
**Action:** Use a cumulative boolean mask (`mask &= ...`) and filter once at the end. Compute on the active subset using `df.loc[mask, col]`, and use `mask.sum()` to count active rows dynamically.
