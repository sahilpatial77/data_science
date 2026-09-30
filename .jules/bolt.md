## 2023-10-24 - Pandas Datetime Optimization
**Learning:** Using pd.to_datetime with a specific format string (e.g. format='%m/%d/%Y %I:%M:%S %p') is significantly faster than relying on pandas' automatic format inference for large datasets.
**Action:** Always provide the exact datetime format when parsing large date columns to avoid the overhead of format inference.
