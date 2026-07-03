## 2024-07-03 - Avoid sequential DataFrame filtering in pandas loops
**Learning:** Sequential DataFrame filtering (df = df[...]) within loops causes expensive O(N) memory allocations for each iteration.
**Action:** Use a cumulative boolean mask (mask &= ...) and filter once at the end. Use df.loc[mask, col] to compute on the active subset, and use mask.sum() to count active rows dynamically.
