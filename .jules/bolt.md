## 2024-07-27 - Sequential DataFrame Filtering in Pandas Loops
**Learning:** Sequential DataFrame filtering within a loop causes expensive O(N) memory reallocations on each iteration, severely degrading performance on large datasets.
**Action:** Use a cumulative boolean mask inside the loop to aggregate conditions, and perform a single filtering operation at the end. Crucially, calculate intermediate values on the active subset using df.loc[mask, col] to preserve correct functional behavior.
