## 2024-05-18 - Avoid Sequential DataFrame Filtering in Loops
**Learning:** Repeatedly filtering a pandas DataFrame inside a loop (`df = df[...]`) causes expensive O(N) memory allocations on every iteration.
**Action:** Compute a cumulative boolean mask (`mask &= ...`) and apply it once at the end. Calculate intermediate values on the active subset using `df.loc[mask, col]` to prevent regressions.
