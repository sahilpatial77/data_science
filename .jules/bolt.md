## 2024-07-27 - Optimized Outlier Removal
**Learning:** Sequential dataframe filtering inside loops causes expensive O(N) memory allocations, especially on large datasets.
**Action:** Use a cumulative boolean mask to filter the dataframe only once at the end, ensuring calculations inside the loop dynamically reference the actively filtered subset to maintain correct logic.
