## 2024-10-31 - Optimizing Pandas DataFrame Filtering
**Learning:** Sequential DataFrame filtering inside loops causes expensive O(N) memory allocations. Using a cumulative boolean mask and filtering once at the end is much more efficient.
**Action:** Use boolean masks and `df.loc[mask, col]` instead of reassigning dataframes sequentially.
