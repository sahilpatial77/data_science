## 2024-07-27 - Pandas Sequential Filtering Bottleneck
**Learning:** Sequential DataFrame filtering in a loop triggers O(N) memory allocations per iteration. In pandas, this creates significant memory overhead and slowdowns.
**Action:** Use a cumulative boolean mask to compute all conditions in the loop, and apply the filter only once at the end. Calculate intermediate values dynamically on the active subset.
