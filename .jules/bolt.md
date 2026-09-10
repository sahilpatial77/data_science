## 2024-09-05 - Optimizing pandas string operations
**Learning:** When standardizing text across large pandas DataFrames with many repeating values, computing string transformations on unique values using a pure Python dictionary and applying them via `.map()` is significantly faster than using sequential `.str` accessor methods over entire columns.
**Action:** Use unique values mapping and `.map()` for applying string transformations in pandas when column cardinality is lower than row count.
