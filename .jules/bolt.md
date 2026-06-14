## 2024-10-24 - Optimize Pandas Outlier Removal
**Learning:** Sequential DataFrame filtering inside loops creates expensive O(N) memory allocations.
**Action:** Use a cumulative boolean mask (`mask & col_mask`) and evaluate quantiles on progressively masked data (`df.loc[mask, col]`) to avoid intermediate DataFrame recreation.
