## 2024-06-18 - Avoid Sequential DataFrame Filtering for Outliers
**Learning:** In pandas, repeatedly filtering a DataFrame in a loop (e.g., df = df[condition]) triggers expensive O(N) memory allocations and copies for each iteration. Evaluating conditions cumulatively into a boolean mask and applying it once is significantly faster.
**Action:** Use a cumulative boolean mask (e.g., mask &= condition) and compute quantiles on the progressively masked data using .loc[mask, col] instead of sequential DataFrame filtering.
