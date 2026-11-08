## 2024-05-14 - Sequential Boolean Mask Optimization
**Learning:** Iteratively filtering and reallocating DataFrames inside a loop (e.g., `df = df[...]`) causes significant memory allocation and performance overhead. Furthermore, recalculating bounds on already-filtered data changes logical correctness.
**Action:** Use a sequential boolean mask (`mask &= ...`) across iterations and apply it once outside the loop (`df = df[mask]`) to perform a single allocation and maintain correct logical bounds.
