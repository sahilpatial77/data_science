## 2024-05-23 - Avoiding Sequential Dataframe Filtering in Loops
**Learning:** Using sequential dataframe filtering inside loops causes expensive memory allocations per iteration in pandas.
**Action:** Use a cumulative boolean mask within the loop and filter the dataframe once at the end to improve performance and reduce memory usage.
