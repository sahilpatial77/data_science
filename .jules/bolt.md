## 2024-07-27 - Pandas Sequential Filtering
**Learning:** Sequential df = df[...] filtering inside loops causes expensive O(N) memory allocations per iteration in pandas.
**Action:** Use a cumulative boolean mask and filter the DataFrame exactly once at the end. Calculate intermediate values on the active subset using df.loc[mask, col].
