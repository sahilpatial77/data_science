## 2024-07-27 - Pandas O(N) DataFrame Filtering in Loops
**Learning:** Sequential DataFrame filtering (df = df[...]) within loops causes expensive O(N) memory allocations.
**Action:** Use a cumulative boolean mask (mask &= ...) and calculate intermediate values dynamically using df.loc[mask, col] within the loop.
