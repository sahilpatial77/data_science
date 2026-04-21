## 2024-05-18 - Pandas Outlier Sequential Filtering
**Learning:** Sequential DataFrame filtering inside loops causes O(N) memory allocation per iteration. Switching to a simple cumulative boolean mask alters the mathematical behavior as subsequent quantiles compute on unmasked initial data.
**Action:** When filtering iteratively, use a cumulative boolean mask (`mask = mask & col_mask`) to avoid the DataFrame allocation overhead, and compute subsequent quantile limits progressively with `df.loc[mask, col].quantile(q)`.
