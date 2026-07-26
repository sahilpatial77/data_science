## 2024-05-20 - Avoid Sequential DataFrame Filtering in Loops
**Learning:** Sequential filtering of pandas DataFrames (e.g., df = df[...]) within loops causes expensive O(N) memory allocations per iteration.
**Action:** Use a cumulative boolean mask (mask &= ...) and apply it once at the end. Calculate intermediate values on the progressively filtered subset using df.loc[mask, col].