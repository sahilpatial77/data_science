## 2024-05-30 - Optimize pandas dataframe memory allocations
**Learning:** In pandas, switching from sequential DataFrame filtering to a simple cumulative boolean mask for outlier removal changes the underlying mathematical behavior. To optimize performance (avoiding O(N) DataFrame memory allocations) while preserving progressive filtering behavior, evaluate boolean masks cumulatively and compute quantiles on the progressively masked data (e.g., `df.loc[mask, col]`).
**Action:** Use cumulative boolean masks with progressively masked data for sequential dataframe filtering.
