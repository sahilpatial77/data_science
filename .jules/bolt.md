## 2024-07-27 - Sequential DataFrame filtering within loops
**Learning:** In pandas scripts, avoid sequential DataFrame filtering (`df = df[...]`) within loops, as it causes expensive O(N) memory allocations. Use a cumulative boolean mask (`mask &= ...`) and filter once at the end.
**Action:** Calculate intermediate values dynamically on the active subset using `df.loc[mask, col]` within the loop, ensuring subsequent calculations account for the progressively filtered dataset.
