## 2024-05-18 - Optimized pd.to_datetime parsing in Pandas
**Learning:** When using pd.to_datetime on large datasets, omitting the exact format string forces Pandas to fallback to inferring the format using dateutil, which results in a significant performance penalty (e.g. ~30% slower).
**Action:** Always explicitly specify the date format string (e.g. format='%m/%d/%Y %I:%M:%S %p') in pd.to_datetime if the dataset's date schema is known, to bypass inference and speed up parsing.
