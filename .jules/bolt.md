## 2024-11-20 - Sequential DataFrame Filtering Overhead
**Learning:** Repeatedly filtering DataFrames inside a loop (e.g., df = df[...]) causes expensive O(N) memory allocations per iteration in pandas.
**Action:** Use a cumulative boolean mask (mask &= ...) and filter the DataFrame once at the end, dynamically calculating intermediate values on the active subset using df.loc[mask, col].
