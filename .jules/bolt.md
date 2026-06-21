## 2024-05-24 - Pandas Outlier Removal Optimization
**Learning:** Sequential DataFrame filtering inside loops (`df = df[...]`) is highly inefficient as it causes O(N) memory allocations and intermediate DataFrame creations per iteration.
**Action:** Use a cumulative boolean mask (`mask &= ...`) and filter the DataFrame once at the end instead to achieve significant speedups, especially for wide DataFrames.
