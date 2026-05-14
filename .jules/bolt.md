## 2024-05-15 - Progressive Outlier Removal
**Learning:** Sequential DataFrame filtering for outlier removal causes repeated O(N) memory allocations and full data copying on each loop iteration.
**Action:** Use a cumulative boolean mask `mask = pd.Series(True, index=df.index)` and compute quantiles on the progressively masked data `df.loc[mask, col]` to avoid dataframe copying while preserving progressive mathematical behavior.
