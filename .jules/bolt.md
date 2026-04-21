## 2024-05-18 - Pandas Outlier Removal Optimization
**Learning:** Sequential DataFrame reassignment within a loop (`df = df[...]`) triggers O(N) memory reallocations, representing a massive performance and memory bottleneck for large datasets.
**Action:** Replace iterative DataFrame filtering with a single cumulative boolean mask. When progressive filtering is mathematically required (e.g., calculating quantiles on a shrinking subset), evaluate the mask cumulatively and slice the target column via `df.loc[mask, col]`. Apply the final mask to the DataFrame only once outside the loop.
