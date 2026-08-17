## 2024-05-24 - Avoid Sequential Pandas Filtering in Loops
**Learning:** In pandas scripts, sequential DataFrame filtering (df = df[...]) within loops causes expensive O(N) memory allocations on each iteration, scaling poorly for large datasets.
**Action:** Use a cumulative boolean mask (mask &= ...) to filter the DataFrame once at the end, while calculating intermediate values dynamically using df.loc[mask, col] to prevent functional regressions.
