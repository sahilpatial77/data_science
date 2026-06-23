## 2025-02-20 - Boolean Mask Optimization for Pandas Filtering
**Learning:** In pandas data processing scripts, sequential DataFrame filtering within loops (`df = df[...]`) causes expensive O(N) memory allocations per iteration.
**Action:** Use a cumulative boolean mask (`mask &= ...`) and filter once at the end. When loop logic (like calculating quantiles) depends on the progressively filtered dataset, use `df.loc[mask, col]` to perform the calculation on the active subset, avoiding regressions while maintaining performance.
