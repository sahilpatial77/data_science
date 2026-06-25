## 2024-06-25 - Avoid Sequential DataFrame Filtering
**Learning:** In pandas data processing scripts, sequential DataFrame filtering (`df = df[...]`) within loops causes expensive O(N) memory allocations, degrading performance significantly on large datasets.
**Action:** Use a cumulative boolean mask (`mask &= ...`) and filter once at the end. If loop logic (like quantiles) depends on the progressively filtered dataset, use `df.loc[mask, col]` to compute on the active subset to maintain functional correctness.
