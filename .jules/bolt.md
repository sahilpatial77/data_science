## 2024-03-24 - Pandas Outlier Removal Optimization
**Learning:** Repeatedly filtering and reallocating DataFrames inside a loop (`df = df[...]`) causes significant memory and performance overhead in Pandas, scaling non-linearly with data size (e.g., 4x slower for 5M rows).
**Action:** Compute a sequential boolean mask across iterations (`mask &= ...`) and apply it outside the loop (`df = df[mask]`) to perform a single allocation. Ensure dependent statistics (like quantiles) are calculated only on the remaining valid rows (`df.loc[mask, col]`) to maintain correctness.
