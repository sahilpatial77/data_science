## 2025-02-28 - Pandas Loop Allocation Overhead
**Learning:** Sequential DataFrame filtering inside loops causes expensive O(N) memory allocations per iteration, dramatically slowing down operations like outlier removal.
**Action:** Use a cumulative boolean mask to evaluate the active rows, compute intermediate statistics with `df.loc[mask, col]`, and apply the filter only once at the end.
