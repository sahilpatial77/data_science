## 2024-07-04 - Cumulative Mask Optimization
**Learning:** Sequential DataFrame filtering inside loops triggers expensive O(N) memory allocations.
**Action:** Use a cumulative boolean mask and calculate statistics on the active subset.
