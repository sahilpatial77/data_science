## 2024-07-16 - Avoid Sequential DataFrame Filtering in Pandas Loops
**Learning:** In pandas data processing scripts, sequential DataFrame filtering (`df = df[...]`) within loops causes expensive O(N) memory allocations and slow performance.
**Action:** Use a cumulative boolean mask (`mask &= ...`) and filter the DataFrame once at the end. Use `df.loc[mask, col]` to compute on the active subset, and use `mask.sum()` to count active rows dynamically.
