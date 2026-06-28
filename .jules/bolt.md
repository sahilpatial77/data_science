## 2024-06-28 - Avoid Sequential DataFrame Filtering
**Learning:** Sequential DataFrame filtering inside loops causes expensive O(N) memory allocations.
**Action:** Use a cumulative boolean mask and filter once at the end.
