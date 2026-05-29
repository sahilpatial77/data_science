## 2024-05-29 - Optimize Outlier Removal
**Learning:** In pandas, switching from sequential DataFrame filtering to a simple cumulative boolean mask for outlier removal changes the underlying mathematical behavior. To optimize performance (avoiding O(N) DataFrame memory allocations) while preserving progressive filtering behavior, evaluate boolean masks cumulatively and compute quantiles on the progressively masked data (e.g., `df.loc[mask, col]`).
**Action:** Use a cumulative boolean mask to prevent O(N) DataFrame memory allocations in loop.
