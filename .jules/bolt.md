## 2024-04-16 - Vectorized vs Sequential Pandas Filtering
**Learning:** Sequential DataFrame updates (e.g., iteratively redefining `df = df[condition]` in a loop over columns) cause O(N) memory allocations because pandas copies the entire dataframe repeatedly.
**Action:** Always compute boolean masks iteratively instead, then apply the single final mask to filter the DataFrame exactly once (`df = df[valid_mask]`). This avoids thrashing memory and speeds up execution significantly, especially for large datasets.
