## 2023-10-24 - Pandas Datetime Parsing Optimization
**Learning:** Using pd.to_datetime without explicitly specifying the format allows Pandas to fall back to dateutil for row-by-row parsing, which scales incredibly poorly on large datasets, causing severe parsing bottlenecks. Hardcoding the known format bypasses the inference entirely.
**Action:** Always inspect the actual datetime strings in the dataset and provide a 'format' argument to pd.to_datetime if a consistent format is known, while retaining errors='coerce' for safety.
