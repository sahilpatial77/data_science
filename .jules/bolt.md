## 2024-05-23 - Cumulative Masking for Outlier Removal
**Learning:** Sequential DataFrame filtering in a loop causes O(N) memory allocations per iteration. Simply switching to a non-progressive mask changes the underlying mathematical behavior of the outlier removal algorithm.
**Action:** Use a cumulative boolean mask (`mask = mask & new_condition`) and compute subsequent metrics (like quantiles) on the progressively masked data (`df.loc[mask, col]`) to avoid reallocation while preserving the mathematical outcome.
