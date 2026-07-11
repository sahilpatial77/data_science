## 2024-07-11 - Cumulative Mask for DataFrame Filtering
**Learning:** Sequential DataFrame filtering within loops (e.g., df = df[...]) triggers O(N) memory allocations per iteration in this pandas pipeline, causing severe performance bottlenecks on large datasets.
**Action:** Always use a cumulative boolean mask (mask &= ...) inside loops and perform a single filtering step at the end (df = df[mask]). Compute intermediate statistics dynamically via df.loc[mask, col] to maintain correctness.
