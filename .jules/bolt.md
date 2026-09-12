## 2026-09-12 - Pandas String Transformation Optimization
**Learning:** When standardizing pandas string columns with repetitive data, computing transformations and space counts on `.unique()` values and applying them via `.map()` is significantly faster than using sequential `.str` accessors across entire columns.
**Action:** Use dictionary mapping on unique values instead of vector string operations for columns with low cardinality.
