## 2024-10-27 - Sequential DataFrame Filtering Bottleneck
**Learning:** Sequential DataFrame filtering (df = df[...]) inside loops causes expensive O(N) memory allocations, drastically slowing down large data processing.
**Action:** Always use a cumulative boolean mask (mask &= ...) for filtering inside loops, calculating intermediate statistics dynamically on the active subset using df.loc[mask, col].
