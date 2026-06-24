## 2024-06-24 - Pandas Boolean Masking Loop Optimization
**Learning:** In pandas data processing scripts, sequential DataFrame filtering (`df = df[...]`) within loops causes expensive O(N) memory allocations for every iteration. Additionally, when loop logic (like quantiles) depends on the progressively filtered dataset, simply computing on the whole frame introduces regressions.
**Action:** Use a cumulative boolean mask (`mask &= ...`) and filter once at the end. To compute on the active subset within the loop to avoid functional regressions, use `df.loc[mask, col]`.
