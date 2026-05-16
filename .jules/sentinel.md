## 2024-05-16 - Unbounded DataFrame Printing
**Vulnerability:** Found an unbounded `print(df)` statement in main.py intended for debugging.
**Learning:** Even though pandas truncates large DataFrames by default, unbounded print statements are treated as potential Denial of Service (DoS) vulnerabilities in this repository because they can still overwhelm logs or console buffers in certain environments or configurations.
**Prevention:** Always restrict DataFrame output using `.head()`, `.tail()`, or remove the print statement entirely.