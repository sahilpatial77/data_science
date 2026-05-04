## 2024-05-24 - Pandas Outlier Filtering Performance
**Learning:** In pandas, sequentially modifying DataFrames within loops (e.g., progressive filtering) causes significant O(N) memory allocation overhead.
**Action:** Prefer evaluating boolean masks cumulatively while preserving exact mathematical behavior by computing quantiles on progressively masked data (e.g., `df.loc[mask, col]`).
