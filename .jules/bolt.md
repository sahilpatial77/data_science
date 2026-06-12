## 2024-05-24 - Outlier Removal Optimization
**Learning:** Sequential DataFrame filtering inside loops for outlier removal causes repeated O(N) memory allocations.
**Action:** Use a cumulative boolean mask (e.g., mask &= condition) and filter the DataFrame once at the end.
