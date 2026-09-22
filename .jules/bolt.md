## 2024-05-18 - Pandas String Operations Optimization
**Learning:** Sequential `.str` accessor methods on large pandas DataFrames with repeated string values are extremely slow.
**Action:** Use `.value_counts()` and pure Python dictionary mapping applied via `.map()` for string transformations to significantly improve performance.
