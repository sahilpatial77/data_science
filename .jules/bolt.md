## 2024-05-24 - Avoid O(N) memory allocations in Pandas filtering loops
**Learning:** Sequential DataFrame filtering within loops causes expensive O(N) memory allocations. Using a cumulative boolean mask and calculating intermediate values dynamically on the active subset is much faster.
**Action:** Use a cumulative boolean mask (`mask &= ...`) and filter once at the end when performing sequential filtering in pandas loops.
