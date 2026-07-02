## 2024-07-02 - Sequential Pandas Filtering is O(N) Memory Intensive
**Learning:** Sequential DataFrame filtering inside loops causes expensive O(N) memory allocations.
**Action:** Use a cumulative boolean mask (mask &= condition) and filter once at the end.
