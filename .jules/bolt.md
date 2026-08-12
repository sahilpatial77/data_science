## 2024-07-27 - [Sequential Pandas Filtering Anti-pattern]
**Learning:** In pandas scripts, avoiding sequential DataFrame filtering (df = df[...]) within loops prevents expensive O(N) memory allocations.
**Action:** Use a cumulative boolean mask (mask &= ...) and filter once at the end, while calculating intermediate values dynamically on the active subset to preserve logic.
