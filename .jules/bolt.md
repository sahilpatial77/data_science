## 2024-05-24 - Pandas Loop Optimization
**Learning:** Sequential DataFrame filtering (`df = df[...]`) within a loop causes expensive O(N) memory allocations, slowing down data processing.
**Action:** Use a cumulative boolean mask (`mask &= ...`) and filter once at the end, while ensuring loop logic that depends on the progressively filtered dataset uses `df.loc[mask, col]` to compute on the active subset.
