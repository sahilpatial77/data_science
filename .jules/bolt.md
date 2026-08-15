## 2024-05-15 - Optimize sequential DataFrame filtering
**Learning:** In pandas, sequential DataFrame filtering within a loop (`df = df[...]`) causes expensive O(N) memory allocations per iteration.
**Action:** Use a cumulative boolean mask (`mask &= ...`) and calculate intermediate statistics dynamically on the active subset (`df.loc[mask, col]`) to progressively filter the dataset while avoiding O(N) allocations.
