## 2024-05-24 - Pandas Sequential Filtering Performance Anti-Pattern
**Learning:** Sequential DataFrame filtering (df = df[...]) inside a loop causes expensive O(N) memory allocations.
**Action:** Use a cumulative boolean mask (mask &= ...) within the loop and filter the DataFrame strictly once at the end. To avoid functional regressions, calculate intermediate quantiles dynamically on the actively filtered subset using df.loc[mask, col].
