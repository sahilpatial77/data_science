## 2023-10-24 - Pandas Outlier Removal Optimization
**Learning:** Repeatedly filtering and reallocating Pandas DataFrames inside a loop (e.g., df = df[...]) causes significant memory overhead. Furthermore, when computing sequential masks, subsequent iterations (like calculating quantiles) must only evaluate the remaining valid rows (e.g., df.loc[mask, col]) rather than the original unfiltered dataset to maintain mathematical correctness.
**Action:** Compute a sequential boolean mask across iterations (e.g., mask &= ...) and apply it outside the loop to perform a single allocation.
