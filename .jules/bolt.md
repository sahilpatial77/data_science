## 2024-06-11 - Pandas Outlier Removal Optimization
**Learning:** For outlier removal in pandas, using sequential DataFrame filtering within a loop causes O(N) memory allocations per iteration, making it inefficient.
**Action:** Evaluate boolean masks cumulatively and compute quantiles on the progressively masked data (e.g., df.loc[mask, col]) instead of using sequential DataFrame filtering.
