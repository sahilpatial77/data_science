## 2024-07-18 - Pandas Sequential Filtering Anti-pattern
**Learning:** Sequential DataFrame filtering (df = df[...]) within a loop causes expensive O(N) memory allocations. In this codebase, it's particularly noticeable in the outlier removal step.
**Action:** Use a cumulative boolean mask (mask &= ...) and filter once at the end. Crucially, calculate intermediate values dynamically on the active subset using df.loc[mask, col] within the loop to ensure correct functionality.
