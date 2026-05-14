## 2024-05-23 - Unbounded DataFrame Printing DoS
**Vulnerability:** Unbounded `print(df)` used for dataset display.
**Learning:** Even though pandas has default truncation, the project specifically treats unbounded dataframe printing as a DoS vulnerability due to memory/CPU consumption risks with large datasets.
**Prevention:** Always use `.head()`, `.tail()`, or remove full DataFrame print statements entirely.
