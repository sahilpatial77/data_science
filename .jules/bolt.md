## 2024-05-24 - Progressive Pandas Filtering
**Learning:** In pandas, simple cumulative boolean masking changes the mathematical behavior of outlier removal compared to sequential DataFrame filtering because quantiles change as rows are removed.
**Action:** When avoiding O(N) DataFrame memory allocations in loops, evaluate boolean masks cumulatively but compute quantiles on the progressively masked data (e.g., `df.loc[mask, col]`) to preserve exact original behavior.
