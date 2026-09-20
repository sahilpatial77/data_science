## 2024-09-05 - Optimize string cleaning with map and unique
**Learning:** For large pandas DataFrames with repeating values, calculating transformations on `.unique()` values using a pure Python dictionary and applying them via `.map()` is significantly faster than using sequential `.str` accessor methods over entire columns. Computing aggregate conditions via `.value_counts()` and iterating in pure Python is also much faster.
**Action:** When operating on string columns containing many repeated values, replace chained `.str` accessors with dictionary mapping over unique values.
