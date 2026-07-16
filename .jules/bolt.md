## 2025-02-18 - Pandas DataFrame Filtering Bottleneck
**Learning:** Sequential DataFrame filtering inside loops causes expensive O(N) memory allocations.
**Action:** Use a cumulative boolean mask inside loops and filter the DataFrame once at the end.
