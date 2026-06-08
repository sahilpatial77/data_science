## 2024-06-08 - Avoid Sequential DataFrame Filtering in Outlier Removal
**Learning:** Sequential DataFrame filtering inside loops causes O(N) memory allocations and severely degrades performance. Evaluating boolean masks cumulatively and computing quantiles on progressively masked data avoids these allocations.
**Action:** Use cumulative boolean masks (e.g., df.loc[mask, col]) instead of recreating the DataFrame repeatedly when filtering multiple columns.
