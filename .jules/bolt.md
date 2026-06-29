## 2024-05-23 - Memory Allocation in Pandas Loops
**Learning:** Sequential DataFrame filtering (`df = df[...]`) within loops causes expensive O(N) memory allocations per iteration in pandas, which is a significant performance bottleneck in data processing scripts.
**Action:** Use a cumulative boolean mask (`mask &= ...`) and filter once at the end. Use `df.loc[mask, col]` to compute on the active subset, and use `mask.sum()` to dynamically count active rows.
