## 2024-05-18 - Optimization: Avoid O(N) memory allocations in DataFrame loops
**Learning:** Sequential DataFrame filtering in pandas loops (e.g., df = df[...]) creates expensive O(N) memory allocations.
**Action:** Use a cumulative boolean mask (mask &= ...) and calculate intermediate values dynamically on the active subset (df.loc[mask, col]), then filter once at the end.
