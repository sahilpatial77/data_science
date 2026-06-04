## 2024-05-24 - Pandas Series Property Optimization
**Learning:** Testing for existence of null values on an entire DataFrame column using `df[col].isnull().sum() > 0` causes an unnecessary full O(N) column traversal and sum computation, allocating temporary boolean arrays.
**Action:** Always prefer the `.hasnans` property on pandas Series for existence checks of missing values, which utilizes early-exit strategies and cached attributes to significantly reduce memory overhead and execution time.
