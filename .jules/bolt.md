## 2024-06-12 - Cumulative Masking for Pandas Outlier Removal
**Learning:** Sequentially filtering a pandas DataFrame in a loop (e.g., df = df[condition]) incurs significant O(N) memory allocation and copy overhead per iteration, degrading performance on large datasets with many numeric columns.
**Action:** Use a cumulative boolean mask (e.g., mask &= condition) and apply it once at the end of the loop, using df.loc[mask, col] within the loop to compute progressive statistics correctly without recreating the DataFrame.
