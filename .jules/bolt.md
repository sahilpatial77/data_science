## 2024-09-05 - Optimize Pandas String Operations
**Learning:** When optimizing string operations on large pandas DataFrames with repeating values, computing transformations on `.unique()` values using a pure Python dictionary and applying them via `.map()` is significantly faster than using sequential `.str` accessor methods over entire columns.
**Action:** Use dictionary mapping and `.map()` for standardizing string columns containing many repeated strings to improve performance.
