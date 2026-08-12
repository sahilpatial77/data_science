## 2024-07-27 - Batch DataFrame filtering in pandas loops
**Learning:** Sequential DataFrame filtering (df = df[...]) within loops causes expensive O(N) memory allocations in pandas.
**Action:** Use a cumulative boolean mask (mask &= ...) and filter once at the end. Calculate intermediate values dynamically on the active subset using df.loc[mask, col] within the loop.
