## 2024-05-24 - Avoiding O(N) DataFrame Allocations
**Learning:** Sequential DataFrame filtering inside a column iteration loop causes expensive O(N) memory allocations per iteration, making it a severe performance anti-pattern in Pandas data processing.
**Action:** Use a cumulative boolean mask (`mask &= ...`) within the loop, compute intermediate statistics on the active subset using `df.loc[mask, col]`, and apply the mask only once at the end of the loop.
