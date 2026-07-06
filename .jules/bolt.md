## 2024-05-24 - Pandas DataFrame Filtering in Loops
**Learning:** Sequential DataFrame filtering (`df = df[...]`) within loops causes expensive O(N) memory allocations on each iteration.
**Action:** Use a cumulative boolean mask (`mask &= ...`) instead, computing quantiles only on active rows via `df.loc[mask, col]`, and filter the DataFrame once at the end.
