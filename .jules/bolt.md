## 2024-05-23 - Optimize Outlier Removal
**Learning:** Sequential DataFrame filtering in pandas creates O(N) memory allocations per column. It is more efficient to evaluate boolean masks cumulatively and compute quantiles on progressively masked data.
**Action:** Use a cumulative boolean mask (e.g., `df.loc[mask, col]`) instead of sequential DataFrame filtering when removing outliers across multiple columns.
