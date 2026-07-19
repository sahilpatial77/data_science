## 2024-05-18 - Pandas Progressive Filtering
**Learning:** In pandas scripts, avoiding sequential DataFrame filtering (df = df[...]) within loops avoids expensive O(N) memory allocations. However, we must compute intermediate values dynamically on the active subset using df.loc[mask, col] within the loop to ensure calculations account for progressively filtered datasets, preventing functional regressions.
**Action:** Use a cumulative boolean mask (mask &= ...) and filter once at the end, while calculating intermediate values on df.loc[mask, col].
