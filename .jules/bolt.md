## 2024-07-27 - [Pandas DataFrame Filtering Bottleneck]
**Learning:** Sequential DataFrame filtering inside loops (df = df[...]) causes massive O(N) memory allocations due to dataframe copies, severely impacting performance for large datasets.
**Action:** Always use cumulative boolean masks (mask &= ...) when evaluating multiple filtering conditions in a loop and apply the mask once at the end.
