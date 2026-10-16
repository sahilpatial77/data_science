## 2023-10-24 - Pandas to_datetime Optimization
**Learning:** When using pd.to_datetime in Pandas, omitting the datetime format causes a severe performance bottleneck because it falls back to the slow dateutil parser.
**Action:** Always specify the exact format (e.g., format='%m/%d/%Y %I:%M:%S %p') when parsing large datetime columns to bypass inference and achieve a ~18x speedup.
