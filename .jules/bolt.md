## 2024-05-18 - Optimize pandas loop filtering
**Learning:** Sequential DataFrame filtering (df = df[...]) within loops causes expensive O(N) memory allocations.
**Action:** Use a cumulative boolean mask (mask &= ...) and filter once at the end. Calculate intermediate values dynamically on the active subset using df.loc[mask, col] to prevent functional regressions.
