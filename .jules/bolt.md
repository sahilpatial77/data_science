## 2024-07-05 - Avoid sequential DataFrame filtering in loops
**Learning:** In pandas data processing scripts, sequential DataFrame filtering (df = df[...]) within loops causes expensive O(N) memory allocations.
**Action:** Use a cumulative boolean mask (mask &= ...) and filter once at the end. Use df.loc[mask, col] to compute on the active subset, and use mask.sum() to count active rows dynamically.
