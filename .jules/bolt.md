## 2024-05-19 - Cumulative Masking for Pandas Outlier Removal
**Learning:** Sequential DataFrame filtering in a loop (`df = df[condition]`) causes O(N * C) memory allocations and index rebuilds because Pandas copies the remaining data on every iteration.
**Action:** Use a cumulative boolean mask (`mask &= condition`) to evaluate conditions iteratively, applying the final mask to filter the DataFrame exactly once outside the loop (`df = df[mask]`), avoiding redundant allocations and saving memory.
