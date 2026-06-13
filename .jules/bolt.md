## 2024-06-13 - [Sequential DataFrame Filtering Bottleneck]
**Learning:** Sequential DataFrame filtering in loops creates unnecessary O(N) memory allocations and intermediate copies.
**Action:** Use cumulative boolean masking to track valid rows and apply the mask once, while computing progressive statistics on df.loc[mask, col].
