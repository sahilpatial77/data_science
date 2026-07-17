## 2024-05-23 - Avoid Sequential DataFrame Filtering
**Learning:** Sequential DataFrame filtering inside loops causes expensive O(N) memory allocations and intermediate copies, significantly slowing down processing in this codebase.
**Action:** Use a cumulative boolean mask and filter the DataFrame once at the end instead.
