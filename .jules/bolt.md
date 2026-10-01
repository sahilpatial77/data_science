## 2024-10-24 - Optimizing pd.to_datetime Parsing
**Learning:** Using pd.to_datetime without specifying a format parameter causes Pandas to fallback to slow format inference (dateutil) for each row. In datasets with many dates, this causes severe bottlenecking.
**Action:** Always specify the exact datetime format (e.g., format='%m/%d/%Y %I:%M:%S %p') when calling pd.to_datetime on string columns to enable fast C-level parsing.
