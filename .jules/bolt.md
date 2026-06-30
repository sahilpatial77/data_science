## 2024-05-24 - Pandas Sequential Filtering Memory Leak
**Learning:** In pandas data processing scripts (e.g., `main.py`), sequential DataFrame filtering (`df = df[...]`) within loops causes expensive O(N) memory allocations.
**Action:** Use a cumulative boolean mask (`mask &= ...`) and filter once at the end. Use `df.loc[mask, col]` to compute on the active subset, and use `mask.sum()` (instead of `df.shape[0]`) to count active rows dynamically.
