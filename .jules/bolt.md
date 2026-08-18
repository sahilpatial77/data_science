## 2024-07-27 - Pandas Loop Allocation Bottleneck
**Learning:** Sequential DataFrame filtering in loops causes expensive O(N) memory allocations, leading to a performance bottleneck specific to this codebase's architecture.
**Action:** Use a cumulative boolean mask (`mask &= ...`) and filter once at the end, while calculating intermediate values dynamically on the active subset using `df.loc[mask, col]` within the loop.
