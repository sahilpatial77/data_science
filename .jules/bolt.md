## 2024-04-30 - Pandas Outlier Removal Optimization
**Learning:** Sequential DataFrame filtering inside loops causes O(N) memory allocation overhead for each iteration. Simply switching to a non-progressive mask changes the underlying mathematical behavior.
**Action:** Evaluate boolean masks cumulatively (`mask &= condition`) and compute quantiles on progressively masked data (`df.loc[mask, col]`) to avoid reallocation while preserving behavior.
