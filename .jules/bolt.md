## 2024-07-27 - Optimize Outlier Removal
**Learning:** In pandas, sequential DataFrame filtering inside loops causes expensive O(N) memory allocations. Using a cumulative boolean mask and filtering once at the end is significantly faster.
**Action:** Use boolean masks for iterative filtering operations instead of reassigning the DataFrame.
