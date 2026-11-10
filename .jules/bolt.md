## 2024-11-10 - Pandas Loop Reallocation Overhead
**Learning:** Iteratively filtering and reallocating Pandas DataFrames inside a loop (e.g., `df = df[...]`) creates significant memory and performance overhead. Furthermore, replacing `pd.Series.quantile()` with `np.nanpercentile()` is significantly faster and maintains behavior with missing data.
**Action:** Use a sequential boolean mask (`mask &= ...`) and filter the DataFrame once outside the loop. Use `np.nanpercentile()` for quantile calculations when appropriate.
