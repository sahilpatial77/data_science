## 2023-10-24 - Pandas to_datetime performance optimization
**Learning:** When using pd.to_datetime in Pandas, not specifying a format forces Pandas to infer the format for each element. This inference is very slow. In a test with 500k unique dates, skipping inference by explicitly setting `format='%m/%d/%Y %I:%M:%S %p'` reduced parsing time from 57s to 2.7s (a ~20x speedup).
**Action:** Always provide an explicit format string to pd.to_datetime when the datetime format is known and consistent, especially for large datasets. Retain `errors='coerce'` to safely handle invalid rows.
