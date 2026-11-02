## 2024-11-20 - Sequential Boolean Mask Optimization
**Learning:** Repeatedly filtering and reallocating DataFrames inside a loop (e.g., `df = df[...]`) causes significant memory and performance overhead.
**Action:** Compute a sequential boolean mask across iterations (e.g., `mask &= ...`) and apply it outside the loop (e.g., `df = df[mask]`) to perform a single allocation.
