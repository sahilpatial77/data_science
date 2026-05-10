## 2024-05-24 - Cumulative Boolean Masking for Pandas
**Learning:** Sequentially filtering DataFrames in loops (e.g., for outlier removal) creates O(N) memory allocations per iteration.
**Action:** Evaluate boolean masks cumulatively and compute quantiles on the progressively masked data (`df.loc[mask, col]`) to avoid reallocation overhead while preserving mathematical behavior.
