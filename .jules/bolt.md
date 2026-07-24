## 2024-05-18 - Pandas Outlier Filtering Performance
**Learning:** Sequential DataFrame filtering inside a loop causes expensive O(N) memory allocations. By using a cumulative boolean mask and updating quantiles dynamically on the active subset, we avoid recreating the dataframe on every iteration.
**Action:** Use a boolean mask updated via mask &= ... and apply it once at the end when filtering datasets in a loop. Calculate intermediate values on df.loc[mask, col] to preserve correctness.
