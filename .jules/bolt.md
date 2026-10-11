## 2024-10-24 - Speeding up datetime parsing
**Learning:** When using pd.to_datetime in pandas, specifying the exact format significantly improves parsing speed because it bypasses the date inference mechanism which is slow.
**Action:** Use the format argument in pd.to_datetime whenever the date format is known and consistent.
