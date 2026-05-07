## 2024-05-24 - Pandas Outlier Removal Memory Allocation
**Learning:** Sequential DataFrame filtering inside loops causes O(N) memory allocation overhead due to continuous DataFrame copies. A naive cumulative mask changes the mathematical behavior of progressive filtering.
**Action:** Evaluate boolean masks cumulatively and compute quantiles on progressively masked data (e.g., `df.loc[mask, col]`) to avoid overhead while preserving the progressive mathematical behavior.
