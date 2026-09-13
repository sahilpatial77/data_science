## 2024-09-05 - Optimize String Operations on Categorical Data
**Learning:** When cleaning large pandas string columns with repeating values (e.g., categories), computing transformations on unique values and applying them via `.map()` is significantly faster than using sequential `.str` accessor methods over the entire column.
**Action:** Use `.value_counts()` and a dictionary map for string standardizations on high-cardinality categorical data instead of `.str.lower()` or `.str.strip()`.
