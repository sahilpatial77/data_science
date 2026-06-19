## 2025-02-20 - [Optimize DataFrame Filtering]
**Learning:** Sequential filtering of a DataFrame inside a loop (`df = df[condition]`) creates expensive copies and incurs O(N) memory allocations per iteration.
**Action:** Use a cumulative boolean mask (`mask = pd.Series(True, index=df.index)`) and apply it only once at the end (`df = df[mask]`). When evaluating values within the loop based on the progressively reduced dataset, apply the mask dynamically to the columns using `df.loc[mask, col]`.
