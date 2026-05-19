## 2024-05-19 - Pandas DataFrame Sequential Filtering Overhead
**Learning:** Sequentially filtering a DataFrame inside a loop causes O(N) memory allocations per iteration and slows down processing.
**Action:** Maintain a boolean mask and filter the DataFrame once at the end, while using df.loc[mask, col] to preserve progressive computation behavior.