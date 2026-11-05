## 2024-05-14 - Optimize DataFrame Filtering Loop
**Learning:** Repeatedly filtering and reallocating DataFrames inside a loop (e.g., `df = df[...]`) causes significant memory and performance overhead.
**Action:** Instead, compute a sequential boolean mask across iterations (e.g., `mask &= ...`) and apply it outside the loop (e.g., `df = df[mask]`) to perform a single allocation. Ensure dependent statistics (like quantiles) are calculated only on the remaining valid rows (e.g., `df.loc[mask, col]`).
