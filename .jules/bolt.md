## 2024-07-27 - Sequential DataFrame Filtering Anti-Pattern
**Learning:** Sequential DataFrame filtering inside loops causes expensive O(N) memory allocations per iteration in pandas, leading to significant performance degradation.
**Action:** Use a cumulative boolean mask and filter the DataFrame once at the end, while calculating intermediate values dynamically on the active subset.
