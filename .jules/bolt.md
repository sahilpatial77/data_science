## 2024-05-24 - Outlier Removal Optimization
**Learning:** Sequential DataFrame filtering inside a loop creates O(N) memory allocations, leading to performance issues.
**Action:** Use a cumulative boolean mask to compute changes on the active subset, applying the filter only once at the end.
