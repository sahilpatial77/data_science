## 2024-10-25 - Pandas Outlier Removal Optimization
**Learning:** Sequential DataFrame filtering inside loops causes O(N) memory allocations, which creates a significant bottleneck. However, simply switching to a single boolean mask changes the mathematical behavior because quantiles need to be computed on the progressively filtered data.
**Action:** Use a cumulative boolean mask to avoid O(N) memory allocations, and compute quantiles on the progressively masked data using `df.loc[mask, col]` to preserve the exact progressive filtering behavior.
