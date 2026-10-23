## 2023-10-24 - Optimizing Pandas DataFrame Outlier Masking
**Learning:** Iteratively modifying DataFrames inside a loop over numeric columns for outlier removal forces multiple reallocation passes and redundant size computations, leading to performance bottlenecks.
**Action:** Use a boolean series to calculate the mask concurrently across all columns and apply the filtering operation in a single vectorized pass.
