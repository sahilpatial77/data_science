## 2023-10-24 - Pandas to_datetime Optimization
**Learning:** Explicitly specifying the exact datetime format (e.g., `format='%m/%d/%Y %I:%M:%S %p'`) when using `pd.to_datetime` significantly improves parsing speed by skipping format inference.
**Action:** Always specify the `format` argument in `pd.to_datetime` when the format is known to avoid severe performance degradation.
