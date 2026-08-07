## 2024-08-07 - Optimizing DataFrame Filtering
**Learning:** Sequential DataFrame filtering inside loops causes expensive O(N) memory allocations.
**Action:** Use a cumulative boolean mask and filter the DataFrame once at the end.
