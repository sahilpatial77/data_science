## 2024-11-20 - Pandas pd.to_datetime Optimization
**Learning:** Explicitly specifying the `format` string in `pd.to_datetime` significantly improves parsing speed because it bypasses pandas' internal format inference.
**Action:** When working with large datasets where the date format is known and consistent, always provide the `format` argument to `pd.to_datetime` to optimize parsing performance.
