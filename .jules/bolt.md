## 2024-07-27 - [Pandas DataFrame Performance]
**Learning:** Sequential DataFrame filtering in pandas (e.g., `df = df[...]`) inside a loop over columns causes expensive O(N) memory allocations.
**Action:** Use a cumulative boolean mask (`mask &= ...`) and filter the DataFrame once at the end. Crucially, calculate intermediate values on the active subset (`df.loc[mask, col]`) to preserve correct functional behavior.
