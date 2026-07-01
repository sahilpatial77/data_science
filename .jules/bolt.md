## 2024-07-01 - DataFrame Filtering Memory Allocation
**Learning:** Sequential DataFrame filtering inside loops causes expensive O(N) memory allocations and copies for each iteration.
**Action:** Use a cumulative boolean mask and filter the DataFrame once at the end, using loc on the active subset.
