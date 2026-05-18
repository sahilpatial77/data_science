## 2024-05-24 - Avoid O(N) DataFrame Allocations in Sequential Filtering
**Learning:** Sequentially filtering DataFrames within loops causes O(N) memory allocations. Using a cumulative boolean mask changes mathematical behavior if quantiles aren't computed on the progressively masked subset.
**Action:** Optimize performance by using a cumulative boolean mask while computing quantiles on progressively masked data (e.g. df.loc[valid_mask, col]).
