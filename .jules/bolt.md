## 2024-09-05 - Optimize Pandas String Operations
**Learning:** Applying string transformations via `.map()` with a dictionary of `.unique()` values is significantly faster than using sequential `.str` accessors across entire large columns with repeating values.
**Action:** Use dictionary mapping on unique values for string transformations in large Pandas DataFrames to improve performance.
