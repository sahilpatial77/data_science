## 2024-07-04 - Avoid Sequential DataFrame Filtering
**Learning:** Sequential DataFrame filtering in pandas loops causes expensive O(N) memory allocations.
**Action:** Use a cumulative boolean mask and filter once at the end, updating the mask with bitwise operations, using mask.sum() to count active rows dynamically.
