## 2024-05-23 - Cumulative Boolean Masks for Outlier Removal
**Learning:** Sequential DataFrame filtering inside loops causes multiple O(N) memory allocations.
**Action:** Use a cumulative boolean mask and compute quantiles on the progressively masked data (e.g., `df.loc[mask, col]`) instead of repeatedly filtering the DataFrame.
