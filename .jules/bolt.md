## 2024-10-24 - Speed up pd.to_datetime parsing
**Learning:** In Pandas, relying on date format inference in pd.to_datetime can be extremely slow. By explicitly passing the exact format string, we skip inference and vastly improve parsing speed.
**Action:** Always provide the format string to pd.to_datetime when the data format is known and uniform across rows.
