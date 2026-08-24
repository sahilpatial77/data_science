## 2024-07-27 - Pandas DataFrame Filtering
**Learning:** Sequential DataFrame filtering inside loops causes expensive O(N) memory allocations.
**Action:** Use a cumulative boolean mask and filter the DataFrame once at the end. Calculate intermediate values dynamically on the active subset using df.loc[mask, col] to ensure correctness.
