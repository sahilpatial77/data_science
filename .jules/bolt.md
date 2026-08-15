## 2024-07-27 - Avoid Sequential Filtering in Pandas Loops
**Learning:** Sequential DataFrame filtering inside loops causes expensive O(N) memory allocations, slowing down performance on large datasets.
**Action:** Use a cumulative boolean mask and filter the DataFrame once at the end, calculating intermediate values dynamically on the active subset.
