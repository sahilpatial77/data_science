## 2024-06-08 - Cumulative Boolean Masks for Outlier Removal
**Learning:** Sequential DataFrame filtering inside loops causes O(N) memory allocations by creating intermediate DataFrame copies.
**Action:** Evaluate boolean masks cumulatively and compute quantiles on the progressively masked data (e.g., df.loc[mask, col]) instead of sequential DataFrame filtering.
