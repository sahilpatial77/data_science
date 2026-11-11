## 2024-11-12 - Vectorizing Outlier Removal
**Learning:** Iteratively modifying DataFrames row-by-row or column-by-column in Pandas by repeatedly reassigning the DataFrame causes expensive O(N) memory copies on every loop iteration, which destroys performance.
**Action:** Use a single boolean mask constructed sequentially to vectorize operations like outlier removal, filtering the DataFrame only once at the end.
