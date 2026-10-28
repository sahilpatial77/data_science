## 2024-10-28 - Optimize Pandas Outlier Removal
**Learning:** Repeatedly filtering and reallocating DataFrames inside a loop (e.g., `df = df[...]`) causes significant memory and performance overhead. Computing a sequential boolean mask across iterations (`mask &= ...`) and applying it outside the loop allows for a single allocation.
**Action:** Use vectorized boolean masking with `np.nanpercentile` instead of `df.quantile` when removing outliers across multiple columns to improve performance.
