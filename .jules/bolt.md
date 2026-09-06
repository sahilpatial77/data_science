## 2024-09-06 - Vectorized String Operations on Unique Values in Pandas
**Learning:** When cleaning large pandas string columns with repetitive values, calculating transformations on unique values and applying them via .map() is significantly faster than executing .str accessor methods over the entire series.
**Action:** Use a dictionary mapping over .unique() elements when applying multiple sequential string transformations (like strip and lower) to large datasets with high repetition.
