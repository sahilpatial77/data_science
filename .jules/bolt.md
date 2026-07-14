## 2024-05-09 - Avoid sequential DataFrame filtering in pandas loops
**Learning:** Sequential DataFrame filtering inside loops causes expensive O(N) memory allocations.
**Action:** Use a cumulative boolean mask and filter the DataFrame once at the end. Compute statistics on the active subset using df.loc[mask, col] and count active rows with mask.sum().
