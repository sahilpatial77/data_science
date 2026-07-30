## 2024-07-27 - Optimizing Sequential DataFrame Filtering in Loops
**Learning:** In pandas scripts, sequential DataFrame filtering (e.g., df = df[...]) within loops causes expensive O(N) memory allocations and unnecessary copying.
**Action:** Use a cumulative boolean mask (e.g., mask &= ...) and filter once at the end. Calculate intermediate values dynamically on the active subset using df.loc[mask, col] within the loop to prevent functional regressions.
