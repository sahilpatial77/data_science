## 2024-05-24 - Pandas Sequential Filtering
**Learning:** In pandas data processing scripts, sequential DataFrame filtering (e.g., `df = df[...]`) within loops causes expensive O(N) memory allocations and slow performance.
**Action:** Use a cumulative boolean mask (e.g., `mask &= ...`) inside loops and apply the filter once at the end. Use `df.loc[mask, col]` for calculations on the active subset.
