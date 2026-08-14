## 2024-08-14 - Optimize outlier removal filtering
**Learning:** Sequential DataFrame filtering in loops causes expensive O(N) memory allocations, leading to slower execution on large datasets.
**Action:** Use a cumulative boolean mask (mask &= ...) and filter the dataframe once at the end, while calculating intermediate statistics dynamically on the active subset using df.loc[mask, col].
