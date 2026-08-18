## 2024-07-27 - [Optimize Outlier Removal]
**Learning:** In pandas scripts, avoid sequential DataFrame filtering (df = df[...]) within loops as it causes expensive O(N) memory allocations, using a cumulative boolean mask (mask &= ...) dynamically calculated on the active subset instead.
**Action:** Use boolean mask for iterative filtering in pandas rather than allocating new dataframes each time.
