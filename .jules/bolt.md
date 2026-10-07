## 2024-10-07 - pd.to_datetime Optimization
**Learning:** When dealing with string parsing for pandas Datetime, not providing explicit format drastically reduces the parsing speed, causing pandas to fallback to python dateutil library.
**Action:** Use format='%m/%d/%Y %I:%M:%S %p' argument in pd.to_datetime.
