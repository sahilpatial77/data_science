## 2024-09-03 - Optimize Pandas String Operations
**Learning:** Computing string transformations on `.unique()` values using a pure Python dictionary and applying them via `.map()` is significantly faster than using sequential `.str` accessor methods over entire columns in large pandas DataFrames with repeating values.
**Action:** Use dictionary mapping on unique values instead of chained `.str` accessors for repeated string transformations in pandas.
