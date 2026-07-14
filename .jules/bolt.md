## 2024-05-24 - Pandas Sequential Filtering Memory Allocations
**Learning:** Sequential DataFrame filtering (df = df[...]) inside loops causes expensive O(N) memory allocations for each iteration.
**Action:** Use a cumulative boolean mask (mask &= ...) and filter the DataFrame once at the end outside the loop.
