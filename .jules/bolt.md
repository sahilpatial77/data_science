## 2026-06-23 - Optimize pandas dataframe sequential filtering
**Learning:** In pandas data processing scripts, sequential DataFrame filtering within loops causes expensive O(N) memory allocations. Using a cumulative boolean mask and filtering once at the end is much faster. If loop logic like quantiles depends on the progressively filtered dataset, use df.loc[mask, col] to compute on the active subset.
**Action:** Use a cumulative boolean mask to avoid sequential DataFrame filtering inside loops when possible.
