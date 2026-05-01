## 2026-05-01 - Sequential vs Cumulative DataFrame Filtering
**Learning:** Switching from sequential DataFrame filtering to a simple cumulative boolean mask for outlier removal changes the underlying mathematical behavior because quantiles shift.
**Action:** To optimize performance and avoid O(N) DataFrame memory allocations while preserving progressive filtering behavior, evaluate boolean masks cumulatively and compute quantiles on the progressively masked data (e.g., `df.loc[mask, col]`).
