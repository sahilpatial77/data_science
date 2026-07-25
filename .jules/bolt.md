## 2024-05-24 - Avoiding O(N) Allocations in Pandas Loops
**Learning:** Sequential DataFrame filtering (df = df[...]) inside loops causes expensive O(N) memory allocations and unnecessary data copying.
**Action:** Use a cumulative boolean mask (mask &= ...) and filter once at the end. Calculate intermediate values on the active subset using df.loc[mask, col] to prevent functional regressions.