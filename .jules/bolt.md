## 2024-09-04 - Optimizing Pandas String Operations
**Learning:** When performing string transformations (strip, lower) on large Pandas DataFrames with many repeating values, computing transformations on `.unique()` values using a pure Python dictionary and applying them via `.map()` is significantly faster than using sequential `.str` accessor methods over entire columns.
**Action:** Opt for `.value_counts()` and `.map(dictionary)` instead of sequential `.str` calls for bulk string cleaning operations when the number of unique strings is small compared to the total row count.
