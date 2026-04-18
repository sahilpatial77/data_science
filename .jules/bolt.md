## 2024-04-18 - Optimize Pandas Outlier Removal

**Learning:** When optimizing loop-based DataFrame modifications by using boolean masks cumulatively to avoid O(N) memory allocation overhead, you must compute intermediate statistics (like quantiles) on the currently valid slice of data (`df.loc[valid_mask, col]`) rather than the original data to preserve the exact mathematical behavior of progressively filtered data.
**Action:** Always verify if an optimization that batches or defers operations inadvertently changes the dataset state used for intermediate calculations.
