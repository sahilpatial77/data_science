## 2024-10-04 - Optimize pandas to_datetime
**Learning:** In Pandas, letting pd.to_datetime infer the format of datetime strings is significantly slower than providing the exact format.
**Action:** Always provide the format argument when using pd.to_datetime for faster parsing.
