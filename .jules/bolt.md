## 2024-10-09 - Pandas Date Formatting
**Learning:** Using pd.to_datetime without a format string causes pandas to infer formats element-by-element, leading to severe performance bottlenecks on large datasets.
**Action:** Always specify the exact datetime format (e.g., format='%m/%d/%Y %I:%M:%S %p') to significantly improve parsing speed.
