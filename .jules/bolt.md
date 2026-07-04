## 2024-07-04 - Pandas DataFrame Memory Optimization
**Learning:** Sequential DataFrame filtering (df = df[...]) within loops causes expensive O(N) memory allocations.
**Action:** Use a cumulative boolean mask (mask &= ...) and filter once at the end. Use df.loc[mask, col] to compute on the active subset, and mask.sum() instead of df.shape[0] to count rows.
