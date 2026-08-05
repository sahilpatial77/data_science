## 2024-07-27 - Sequential DataFrame Filtering Optimization
**Learning:** In pandas scripts, sequential DataFrame filtering inside loops causes expensive O(N) memory allocations.
**Action:** Use a cumulative boolean mask and filter the DataFrame once at the end.
