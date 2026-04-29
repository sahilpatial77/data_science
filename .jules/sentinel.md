## 2024-04-29 - Prevent Resource Exhaustion on Print
**Vulnerability:** Unbounded DataFrame printing (`print(df)`) can cause memory exhaustion and crash the application when handling large datasets.
**Learning:** Even local data science scripts should employ basic resource bounding to prevent accidental Denial of Service on the user's machine.
**Prevention:** Always use bounding methods like `df.head(100)` or `df.tail()` when displaying dataframes to standard output.