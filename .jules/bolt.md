## 2024-09-05 - Optimizing Pandas String Operations
**Learning:** When applying string transformations to large Pandas DataFrames with repeating values, computing the transformation on unique values using a pure Python dictionary and applying it via `.map()` is significantly faster than using sequential `.str` accessor methods over the entire column.
**Action:** In future Pandas workflows, check for high cardinality and prioritize dictionary mapping of unique values over `.str` accessor methods for string manipulations.
