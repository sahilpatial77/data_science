## 2024-05-24 - Pandas Sequential Filtering Bottleneck
**Learning:** In pandas data processing scripts, sequential DataFrame filtering (`df = df[...]`) within a loop causes expensive O(N) memory allocations for each iteration.
**Action:** Use a cumulative boolean mask (`mask &= ...`) and filter the DataFrame once at the end of the loop.
