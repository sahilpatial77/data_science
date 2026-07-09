## 2024-07-09 - Pandas Sequential Filtering Anti-Pattern
**Learning:** Sequential DataFrame filtering within loops causes expensive O(N) memory reallocations, which becomes a bottleneck on large datasets.
**Action:** Use a cumulative boolean mask (mask &= ...) and filter the DataFrame once at the end. Compute necessary loop statistics using df.loc[mask, col].
