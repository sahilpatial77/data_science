## 2024-05-18 - Pandas Sequential Filtering Memory Optimization
**Learning:** In pandas, sequential DataFrame filtering (df = df[...]) within loops causes expensive O(N) memory allocations and copies.
**Action:** Always use a cumulative boolean mask (mask &= ...) to track valid rows and perform a single filter at the end, while calculating intermediate loop values dynamically using df.loc[mask, col] on the active subset to maintain correctness.
