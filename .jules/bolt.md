## 2024-07-27 - Cumulative Mask Optimization
**Learning:** Sequential DataFrame filtering inside loops causes expensive O(N) memory allocations.
**Action:** Use a cumulative boolean mask and dynamically calculate intermediate values on the active subset using df.loc[mask, col], filtering the DataFrame only once at the end.