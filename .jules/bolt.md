## 2024-05-20 - Prevent O(N) DataFrame allocations in sequential filtering
**Learning:** Sequentially filtering pandas DataFrames inside loops (e.g., `df = df[condition]`) triggers expensive O(N) memory allocations for each iteration.
**Action:** Use a cumulative boolean mask (`mask &= condition`) and filter the DataFrame once at the end. Ensure intermediate loop calculations (like `.quantile()`) are dynamically evaluated on the active subset using `df.loc[mask, col]` to maintain identical logic.
