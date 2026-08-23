## 2024-07-27 - Pandas Boolean Mask Optimization
**Learning:** In pandas, repeatedly re-assigning a filtered DataFrame inside a loop triggers expensive O(N) memory allocations per iteration.
**Action:** Use a cumulative boolean mask to filter once at the end, and dynamically calculate intermediate statistics on the active subset to prevent functional regressions.
