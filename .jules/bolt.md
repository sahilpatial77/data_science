## 2024-07-27 - Avoid sequential DataFrame filtering in pandas loops
**Learning:** Sequential DataFrame filtering inside a loop triggers O(N) memory allocations repeatedly.
**Action:** Use a cumulative boolean mask and filter the DataFrame once at the end, calculating intermediate values on the active subset.
