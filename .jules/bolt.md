## 2024-07-27 - Sequential DataFrame Filtering Optimization
**Learning:** In pandas scripts, sequential DataFrame filtering (df = df[...]) within loops causes expensive O(N) memory allocations. Crucially, calculating intermediate values dynamically on the active subset using df.loc[mask, col] within the loop prevents functional regressions.
**Action:** Use a cumulative boolean mask (mask &= ...) and filter once at the end, ensuring intermediate calculations are dynamically updated.
