## 2024-05-24 - Optimize sequential DataFrame filtering
**Learning:** Sequential DataFrame filtering inside loops causes expensive O(N) memory allocations.
**Action:** Use a cumulative boolean mask and filter once at the end, using df.loc[mask, col] for intermediate computations.
