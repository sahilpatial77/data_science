## 2024-05-24 - Pandas String Optimization
**Learning:** String operations on pandas DataFrames with large datasets are significantly slower when applied sequentially via .str compared to applying operations using pure Python dictionaries mapped to unique values.
**Action:** Use dictionary mapping on unique values for string cleaning on large datasets.
