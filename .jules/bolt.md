## 2024-08-01 - Avoid Sequential Filtering
**Learning:** Sequential DataFrame filtering in loops causes expensive O(N) allocations.
**Action:** Use a cumulative boolean mask and filter once at the end.
