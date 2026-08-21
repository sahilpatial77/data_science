## 2024-07-27 - Optimize DataFrame Filtering
**Learning:** Sequential DataFrame filtering in loops causes expensive O(N) memory allocations.
**Action:** Use a cumulative boolean mask to filter once at the end, and calculate intermediate values on the active subset.
