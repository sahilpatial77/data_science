## 2026-07-20 - Pandas Loop Dataframe Reallocation
**Learning:** Sequential DataFrame filtering within loops (df = df[...]) causes expensive O(N) memory allocations, negatively impacting performance.
**Action:** Use a cumulative boolean mask (mask &= ...) and filter once at the end. Calculate intermediate values dynamically on the active subset using df.loc[mask, col] within the loop.
