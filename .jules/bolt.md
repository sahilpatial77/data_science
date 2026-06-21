## 2026-06-21 - [Use hasnans over isnull().sum() for existence checks]
**Learning:** For checking existence of missing values in pandas DataFrames and Series, `.hasnans` or `.any()` performs significantly better than `.isnull().sum() > 0` because it benefits from short-circuiting optimization and avoids full-column traversal.
**Action:** Prefer using `.hasnans` or `.isnull().any()` when only checking if any NaNs exist, instead of counting them with `.sum() > 0`.
