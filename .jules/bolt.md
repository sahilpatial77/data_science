## 2026-10-20 - Optimize to_datetime in main.py
**Learning:** In Pandas, implicitly relying on `pd.to_datetime` to infer date formats across large datasets is a severe bottleneck, taking roughly half of the script's execution time due to fallback loops. Specifying `format` allows bypassing inference.
**Action:** Always explicitly specify the exact datetime format (e.g., `format='%m/%d/%Y %I:%M:%S %p'`) when converting strings to datetime objects to improve performance, retaining `errors='coerce'` for safety.
