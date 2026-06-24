## 2025-02-26 - Sequential DataFrame Filtering in Loops
**Learning:** Sequential DataFrame filtering inside loops (`df = df[...]`) causes expensive O(N) memory allocations per iteration.
**Action:** Use a cumulative boolean mask (`mask &= ...`) and filter the DataFrame once at the end. Use `df.loc[mask, col]` to calculate stats dynamically on the active subset.
