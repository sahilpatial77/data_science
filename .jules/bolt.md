## 2024-05-14 - Optimize Pandas DateTime Parsing
**Learning:** In Pandas, specifying the exact format string in pd.to_datetime (e.g., format='%m/%d/%Y %I:%M:%S %p') significantly improves parsing speed by skipping format inference, but it can be brittle if multiple columns have different formats.
**Action:** Always specify the format parameter in pd.to_datetime when the data has a consistent, known datetime format to prevent slow fallbacks to dateutil.
