## 2023-10-24 - Explicit Pandas Datetime Formatting
**Learning:** Relying on Pandas' default dynamic datetime format inference during `pd.to_datetime` can cause massive performance bottlenecks on large datasets.
**Action:** Always explicitly specify the exact `format` string (e.g., `format='%m/%d/%Y %I:%M:%S %p'`) when using `pd.to_datetime` to bypass inference and significantly improve parsing speed.
