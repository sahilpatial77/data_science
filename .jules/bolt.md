## 2024-05-24 - Avoid Sequential DataFrame Filtering in Loops
**Learning:** Sequential DataFrame filtering (e.g., df = df[...]) inside a loop causes expensive O(N) memory allocations for each iteration, becoming a major performance bottleneck for large datasets.
**Action:** Use a cumulative boolean mask (mask &= ...) and calculate intermediate thresholds dynamically on the active subset (df.loc[mask, col]), then apply the mask once at the end of the loop.
