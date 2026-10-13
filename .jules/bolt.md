## 2023-10-24 - Pandas to_datetime Optimization
**Learning:** Specifying the exact datetime format (e.g., `format='%m/%d/%Y %I:%M:%S %p'`) when using `pd.to_datetime` significantly improves parsing speed by skipping format inference, yielding an ~20x performance improvement.
**Action:** Always specify the format parameter when converting strings to datetime objects in pandas if the format is known, while retaining `errors='coerce'` for safety.
