## 2024-05-24 - Avoid O(N) DataFrame memory allocations in loops
**Learning:** Sequential DataFrame filtering in pandas (e.g. `df = df[condition]` in a loop) allocates a new DataFrame each iteration. However, we must preserve progressive filtering mathematical behavior when calculating statistics like quantiles for subsequent iterations.
**Action:** Evaluate boolean masks cumulatively (`mask &= condition`) and compute quantiles on the progressively masked data (`df.loc[mask, col]`). Apply the final mask outside the loop.
