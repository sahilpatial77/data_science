## 2023-10-24 - Pandas to_datetime Performance Bottleneck
**Learning:** Relying on pandas date format inference (without explicitly setting format) causes massive performance degradation on large datasets, as observed with pd.to_datetime.
**Action:** Always specify the exact format string (e.g., format='%m/%d/%Y %I:%M:%S %p') when parsing large datetime columns to skip format inference and boost speed.
