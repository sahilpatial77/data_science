## 2024-05-24 - Preserving Mathematical Behavior in Cumulative Boolean Masking
**Learning:** Switching from sequential DataFrame filtering to a cumulative boolean mask changes the underlying mathematical behavior because quantiles are computed on different data distributions if not careful.
**Action:** Evaluate boolean masks cumulatively and compute quantiles on the progressively masked data using `df.loc[mask, col]` to avoid O(N) allocations while preserving progressive filtering behavior.
