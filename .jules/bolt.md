## 2025-02-14 - Pandas Loop Filtering Anti-pattern
**Learning:** In pandas data processing scripts (e.g., main.py), sequential DataFrame filtering within loops (df = df[...]) causes expensive O(N) memory allocations.
**Action:** Use a cumulative boolean mask (mask &= ...) and filter once at the end, using df.loc[mask, col] to compute on the active subset and mask.sum() to count dynamically.
