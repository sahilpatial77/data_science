## 2024-05-24 - Vectorize O(N) DataFrame copies in outlier removal
**Learning:** Iteratively filtering a pandas DataFrame inside a loop over its columns creates `O(N)` copies of the dataset, acting as a severe performance bottleneck for large data (N+1 query equivalent for DataFrames).
**Action:** Always compute quantiles/bounds using pandas' vectorized operations across all columns at once, construct a single combined boolean mask (e.g. `mask = ((df >= lower) & (df <= upper)).all(axis=1)`), and filter the DataFrame exactly once.
