## 2024-04-24 - DoS Risk in Pandas DataFrame Output
**Vulnerability:** Unbounded `print(df)` found in local data science scripts.
**Learning:** Even in non-web scripts, calling print on massive datasets can cause process hang/crash and memory exhaustion due to terminal buffering and object serialization limits.
**Prevention:** Always bound large data outputs using `.head()`, `.tail()`, `.sample()`, or explicit row limitations when outputting DataFrames to standard output.
