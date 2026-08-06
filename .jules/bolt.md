## 2024-07-27 - Sequential DataFrame Filtering in Pandas
**Learning:** Sequential DataFrame filtering in a loop causes expensive O(N) memory allocations and slows down outlier removal scripts significantly.
**Action:** Use a cumulative boolean mask and update it dynamically on the active subset, then filter the DataFrame once at the end.