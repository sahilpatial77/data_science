## 2024-05-24 - Avoid Sequential DataFrame Filtering
**Learning:** In pandas data processing scripts, sequential DataFrame filtering within loops causes expensive O(N) memory allocations.
**Action:** Use a cumulative boolean mask (`mask &= ...`) and filter once at the end, using `df.loc[mask, col]` to compute on the active subset.
