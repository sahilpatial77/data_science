## 2024-05-24 - Optimized Iterative DataFrame Filtering
**Learning:** Repeatedly filtering and reallocating DataFrames inside a loop (e.g., `df = df[...]`) causes significant memory and performance overhead.
**Action:** Compute a sequential boolean mask across iterations (e.g., `mask &= ...`) and apply it outside the loop to perform a single allocation. Ensure dependent statistics inside the loop are calculated only on the remaining valid rows (e.g., `df.loc[mask, col]`).
