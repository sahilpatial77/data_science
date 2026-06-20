## 2024-06-20 - Sequential DataFrame Filtering Bottleneck
**Learning:** Sequential masking and overwriting of a DataFrame inside a loop (`df = df[condition]`) for outlier removal is computationally expensive due to O(N) intermediate memory allocations and copies.
**Action:** Use a cumulative boolean mask (`mask &= condition`) initialized to `True` for all rows, compute operations conditionally on the valid data, and apply the final mask in a single slice at the end (`df = df[mask]`) to prevent fragmentation and significantly improve performance.
