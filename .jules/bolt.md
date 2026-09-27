## 2023-10-24 - Optimize pd.to_datetime with explicit format
**Learning:** Using `pd.to_datetime` without an explicit format string is significantly slower as pandas has to infer the format for each row.
**Action:** Always provide an explicit format string like `format='%m/%d/%Y %I:%M:%S %p'` when using `pd.to_datetime`.
