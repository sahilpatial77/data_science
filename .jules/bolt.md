## 2024-07-28 - Avoid sequential DataFrame filtering within loops
**Learning:** Sequential DataFrame filtering inside a loop causes expensive O(N) memory allocations, degrading performance significantly.
**Action:** Use a cumulative boolean mask and filter the DataFrame once at the end, ensuring dynamic subsetting within the loop to preserve identical logic.
