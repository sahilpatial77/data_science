## 2024-10-24 - Pandas Sequential Filtering Memory Allocation
**Learning:** In pandas data processing scripts, sequential DataFrame filtering within loops (e.g., df = df[...]) causes expensive O(N) memory allocations. Loop logic like quantile calculation that depends on the progressively filtered dataset can be maintained using a cumulative boolean mask and df.loc[mask, col].
**Action:** Use a cumulative boolean mask (mask &= ...) and filter the DataFrame once at the end to improve performance and reduce memory allocations.
