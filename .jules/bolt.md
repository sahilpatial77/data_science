## 2024-05-24 - Avoid Sequential DataFrame Filtering
**Learning:** In pandas, sequentially filtering a DataFrame inside a loop over multiple columns causes O(N) memory allocations and severely degrades performance due to repeated copy operations.
**Action:** Optimize performance by building a cumulative boolean mask (and computing quantiles progressively with df.loc[mask, col]) to evaluate all conditions before applying the final filter in one step.
