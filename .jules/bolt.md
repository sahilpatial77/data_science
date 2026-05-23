## 2024-05-24 - Cumulative Boolean Masking for Outlier Removal
**Learning:** Sequential DataFrame filtering inside loops causes O(N) memory allocations by creating intermediate DataFrames. Evaluating boolean masks cumulatively while computing quantiles on progressively masked data avoids these allocations while preserving mathematical correctness.
**Action:** Use cumulative boolean masks with `df.loc[mask, col]` for iterative filtering operations instead of reassigning the DataFrame repeatedly.
