## 2024-05-24 - Pandas Sequential Filtering Bottleneck
**Learning:** Sequential DataFrame filtering inside loops (`df = df[...]`) triggers O(N) memory allocation and copy overhead per iteration, significantly slowing down outlier removal.
**Action:** Use a cumulative boolean mask (`mask &= ...`) within the loop and filter the DataFrame once at the end (`df = df[mask]`).
