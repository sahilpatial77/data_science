## 2024-07-27 - Optimize Pandas Filtering in Loops
**Learning:** Avoid sequential DataFrame filtering (`df = df[...]`) inside loops as it causes expensive O(N) memory allocations. Instead, use a cumulative boolean mask and calculate intermediate quantiles dynamically on the active subset via `df.loc[mask, col]`.
**Action:** Apply cumulative boolean masks for sequential filtering conditions to reduce memory overhead and improve execution speed.
