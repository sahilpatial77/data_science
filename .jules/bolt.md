## 2026-09-17 - Optimize Pandas String Operations
**Learning:** Sequential `.str` operations across entire columns in large pandas DataFrames are relatively slow. Computing unique value transformations using a pure Python dictionary and applying them via `.map()` is significantly faster.
**Action:** When performing intensive string cleanup operations on columns with high cardinality or repeated values, use `.value_counts()` and dictionary `.map()` over unique strings instead of chaining multiple `.str` methods.
