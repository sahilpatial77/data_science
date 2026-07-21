## 2024-07-21 - Pandas Sequential Filtering
**Learning:** Sequential DataFrame filtering inside loops causes expensive O(N) memory allocations.
**Action:** Use a cumulative boolean mask and calculate intermediate values dynamically on the active subset.
