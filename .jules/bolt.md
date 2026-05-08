## 2024-05-24 - Pandas Progressive Filtering Overhead
**Learning:** Sequential DataFrame filtering in a loop (e.g., `df = df[condition]`) causes repeated O(N) memory allocations. Switching to a simple boolean mask changes the mathematical behavior of outlier removal since quantiles aren't evaluated on progressively filtered data.
**Action:** Evaluate boolean masks cumulatively (`mask &= new_condition`) and calculate metrics on the progressively masked data using `.loc` (e.g., `df.loc[mask, col]`) to avoid O(N) allocations while preserving exact mathematical behavior.
