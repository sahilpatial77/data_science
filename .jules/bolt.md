## 2024-05-30 - Progressive DataFrame Filtering
**Learning:** Switching from sequential DataFrame filtering to a simple cumulative boolean mask for outlier removal changes the underlying mathematical behavior.
**Action:** To optimize performance avoiding O(N) allocations while preserving progressive filtering behavior, evaluate boolean masks cumulatively and compute quantiles on the progressively masked data.
