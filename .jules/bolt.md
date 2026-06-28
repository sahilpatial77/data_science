## 2024-06-28 - Avoid O(N) memory allocations in Pandas Loops
**Learning:** Sequential DataFrame filtering (df = df[...]) within loops causes expensive O(N) memory allocations. If the loop logic (like quantiles) depends on the progressively filtered dataset, use a cumulative mask and df.loc[mask, col] instead.
**Action:** Use a cumulative boolean mask (mask &= ...) and filter the DataFrame once at the end to prevent memory fragmentation and improve performance.
