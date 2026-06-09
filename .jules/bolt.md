## 2024-05-24 - Pandas Outlier Removal Optimization
**Learning:** Sequential DataFrame filtering inside loops causes O(N) memory allocations and unnecessary data copying, significantly degrading performance.
**Action:** Use cumulative boolean masks and compute operations on progressively masked data (e.g., `df.loc[mask, col]`) instead of sequential DataFrame filtering.
