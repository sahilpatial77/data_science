## 2024-07-23 - Pandas DataFrame Filtering Bottleneck
**Learning:** Sequential DataFrame filtering in loops causes expensive O(N) memory allocations.
**Action:** Use a cumulative boolean mask and filter once at the end, calculating intermediate values on the active subset.
