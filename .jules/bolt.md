## 2024-10-24 - Pandas Sequential Filtering Overhead
**Learning:** Repeatedly filtering and reallocating a Pandas DataFrame inside a loop (`df = df[...]`) introduces significant memory allocation and execution overhead, especially on large datasets.
**Action:** Compute a sequential boolean mask across iterations (`mask &= ...`) and apply it outside the loop (`df = df[mask]`) to perform a single allocation.
