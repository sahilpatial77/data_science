## 2026-06-14 - [Optimize Pandas Outlier Filtering]
**Learning:** Sequential filtering on large pandas DataFrames creates excessive O(N) memory reallocations. Cumulative masking on the original frame is significantly faster.
**Action:** Use cumulative boolean masks and compute quantiles on progressively masked data (df.loc[mask, col]) instead of sequentially applying df = df[...].
