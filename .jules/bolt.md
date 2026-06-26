## 2024-06-26 - Avoid Sequential DataFrame Filtering in Loops
**Learning:** Sequential DataFrame filtering inside loops (e.g., df = df[...]) causes expensive O(N) memory allocations per iteration.
**Action:** Use a cumulative boolean mask (mask &= ...) and filter once at the end, using df.loc[mask, col] to compute quantiles on the active subset.
