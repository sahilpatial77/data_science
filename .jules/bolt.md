## 2026-10-14 - Optimizing pd.to_datetime with format
**Learning:** Using `pd.to_datetime` without explicitly specifying the datetime format causes Pandas to use format inference which falls back to `dateutil` for unknown formats. This can be significantly slower, particularly for large datasets. Hardcoding the format string improves parsing speed considerably (~20x).
**Action:** Always provide the `format` argument when using `pd.to_datetime` if the datetime format is known and consistent across the dataset to avoid the performance penalty of format inference.
