## 2024-08-20 - Sequential Pandas Filtering Optimization
**Learning:** Sequential DataFrame filtering (`df = df[...]`) within loops causes expensive O(N) memory allocations per iteration.
**Action:** Use a cumulative boolean mask (`mask &= ...`) and filter once at the end. Calculate intermediate values on the active subset using `df.loc[mask, col]` to maintain functional equivalence with sequential filtering.
