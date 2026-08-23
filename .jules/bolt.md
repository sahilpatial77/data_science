## 2024-08-23 - Optimize Sequential DataFrame Filtering
**Learning:** Sequential DataFrame filtering (df = df[...]) inside loops causes expensive O(N) memory allocations for each iteration. Calculating quantiles on dynamically filtered subsets while accumulating a boolean mask prevents this overhead and functional regressions.
**Action:** Use a cumulative boolean mask (mask &= ...) and apply the filter once outside the loop instead of sequentially reassigning the dataframe.
