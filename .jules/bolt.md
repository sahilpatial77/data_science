## 2024-05-24 - Pandas Outlier Removal Memory Optimization
**Learning:** Sequential DataFrame filtering inside loops (`df = df[cond]`) causes O(N) memory allocations per iteration. Simply switching to a single boolean mask changes the mathematical result if quantiles are progressively calculated.
**Action:** Evaluate boolean masks cumulatively and compute quantiles on the progressively masked data (e.g., `df.loc[mask, col]`) to avoid memory allocation overhead while preserving progressive filtering behavior.
