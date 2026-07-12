## 2024-05-24 - Optimize pandas filtering in loop
**Learning:** Sequential DataFrame filtering inside loops causes expensive O(N) memory allocations.
**Action:** Use a cumulative boolean mask (`mask &= ...`) and filter once at the end. Use `df.loc[mask, col]` to compute on the active subset, and `mask.sum()` to count active rows dynamically.
