## 2024-07-17 - Pandas Filter Efficiency
**Learning:** Sequential DataFrame filtering inside loops (like `df = df[(df[col] >= lower) & (df[col] <= upper)]`) causes expensive O(N) memory allocations per loop iteration.
**Action:** Use a cumulative boolean mask (`mask &= ...`) and filter once at the end. Use `mask.sum()` to count active rows dynamically.
