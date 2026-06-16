## 2024-05-18 - Optimized Outlier Removal in Pandas

**Learning:** For outlier removal across multiple columns in pandas, sequential DataFrame filtering (`df = df[condition]`) is slow because it creates a new DataFrame copy at each iteration, allocating memory and O(N) operations repeatedly. Evaluating boolean masks cumulatively (`mask &= condition`) and applying it once at the end is significantly faster (measured ~60% reduction in execution time for 5M rows).

**Action:** Whenever iterating over columns to filter rows based on conditions, accumulate the condition in a single boolean mask instead of sequentially applying it to the DataFrame and reassigning. Compute necessary statistics (like quantiles) on `df.loc[mask, col]` to ensure accuracy matching the sequential approach.
