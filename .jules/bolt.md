## 2024-05-24 - Pandas Sequential Filtering Memory Allocation
**Learning:** In pandas data processing scripts (like main.py), sequential DataFrame filtering (df = df[...]) inside loops causes expensive O(N) memory allocations for every iteration, which degrades performance for large datasets.
**Action:** Use a cumulative boolean mask (mask &= ...) inside loops to filter data once at the end, and use df.loc[mask, col] to perform computations on the active subset dynamically.
