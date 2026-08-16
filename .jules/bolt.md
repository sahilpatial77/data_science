## 2024-08-16 - Prevent O(N) Memory Allocations in Pandas Loops
**Learning:** Sequential DataFrame filtering (df = df[...]) inside a loop causes expensive O(N) memory allocations because pandas copies the entire DataFrame on each iteration.
**Action:** Use a cumulative boolean mask (mask &= ...) and calculate intermediate values on the active subset using df.loc[mask, col], then apply the mask once at the end of the loop.
