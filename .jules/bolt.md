## 2024-07-27 - Optimize DataFrame Filtering
**Learning:** Sequential DataFrame filtering in loops causes expensive O(N) memory allocations.
**Action:** Use a cumulative boolean mask (`mask &= ...`) and filter once at the end, calculating intermediate values dynamically with `df.loc[mask, col]` to prevent regressions.
