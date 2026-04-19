## 2024-05-24 - Pandas Sequential Filtering Bottleneck
**Learning:** Sequential DataFrame filtering in a loop causes O(N) memory allocations. Using a cumulative boolean mask and computing quantiles on progressively masked data (e.g., df.loc[mask, col]) optimizes performance while preserving the exact mathematical behavior.
**Action:** Prefer cumulative boolean masks over sequential DataFrame reassignment inside loops to avoid allocation overhead.
