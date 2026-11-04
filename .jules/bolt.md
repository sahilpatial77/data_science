## 2023-10-24 - Avoiding DataFrame Reallocation in Pandas Loops
**Learning:** In Pandas, repeatedly filtering and reallocating DataFrames inside a loop (`df = df[...]`) causes significant memory and performance overhead due to constant reallocation and intermediate arrays, especially for large datasets.
**Action:** Compute a sequential boolean mask across iterations (`mask &= ...`) and apply it outside the loop (`df = df[mask]`) to perform a single allocation. Ensure dependent statistics (like quantiles) inside the loop are computed on `df.loc[mask, col]` to maintain correct bounds.
