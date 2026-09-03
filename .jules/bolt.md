## 2024-09-03 - Optimize string cleaning with dictionary map
**Learning:** When cleaning strings in large Pandas DataFrames with repeating values, computing transformations on `.unique()` values using a pure Python dictionary and applying them via `.map()` is significantly faster than using sequential `.str` accessor methods over entire columns.
**Action:** Always prefer mapping over unique values when applying multiple string operations to categorical-like data columns to avoid redundant computations.
