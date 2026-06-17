## 2024-06-17 - Pandas Outlier Removal Optimization
**Learning:** Sequential DataFrame filtering inside loops for outlier removal incurs O(N) memory allocation and large overhead.
**Action:** Optimize performance by using a cumulative boolean mask and filtering the DataFrame only once at the end. Compute quantiles on the progressively masked data via df.loc[mask, col].
