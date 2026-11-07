## 2024-05-15 - Optimize Outlier Removal
**Learning:** Repeatedly filtering and reallocating DataFrames inside a loop (e.g., `df = df[...]`) causes significant memory overhead and performance degradation.
**Action:** Compute a sequential boolean mask across iterations and apply it outside the loop to perform a single allocation, ensuring that dependent statistics for subsequent iterations are calculated only on the remaining valid rows using `.loc`.
