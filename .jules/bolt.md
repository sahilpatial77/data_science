## 2023-10-24 - Pandas Outlier Removal Optimization
**Learning:** Repeatedly filtering and reallocating DataFrames inside a loop (e.g., `df = df[...]`) causes significant memory and performance overhead.
**Action:** Compute a sequential boolean mask across iterations (e.g., `mask &= ...`) and apply it outside the loop (e.g., `df = df[mask]`) to perform a single allocation, ensuring that dependent statistics (like quantiles) for subsequent iterations are calculated only on the remaining valid rows (e.g., `df.loc[mask, col]`).
