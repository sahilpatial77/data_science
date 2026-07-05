## 2024-05-24 - Pandas Boolean Masking
**Learning:** Iterative DataFrame filtering (df = df[...]) inside a loop causes O(N) memory allocations and is a significant performance bottleneck.
**Action:** Use a cumulative boolean mask (mask &= ...) to compute active rows, and apply the filter exactly once at the end. Use df.loc[mask, col] to compute metrics on the active subset.
