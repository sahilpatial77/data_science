## 2024-09-05 - Fast string cleaning in pandas
**Learning:** Computing transformations on `.unique()` values using a pure Python dictionary and applying them via `.map()` is significantly faster than using sequential `.str` accessor methods over entire columns on large pandas DataFrames with repeating values.
**Action:** Replace sequential `.str` operations with `.value_counts()` aggregation and dictionary `.map()` for string columns with high cardinality.
