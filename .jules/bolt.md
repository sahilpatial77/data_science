## 2024-05-24 - Pandas Outlier Removal Optimization
**Learning:** In pandas, switching from sequential DataFrame filtering to a simple cumulative boolean mask for outlier removal changes the underlying mathematical behavior, because quantiles are computed on the original full dataset instead of the progressively filtered one.
**Action:** To optimize performance (avoiding O(N) DataFrame memory allocations) while preserving progressive filtering behavior, evaluate boolean masks cumulatively and compute quantiles on the progressively masked data (e.g., `df.loc[mask, col]`).
