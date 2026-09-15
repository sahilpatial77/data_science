## 2024-09-16 - Pandas String Operation Optimization
**Learning:** Sequential `.str` accessors on large pandas DataFrames with repeating values are significantly slower than mapping precomputed dictionary transformations on `.unique()` values.
**Action:** When performing multiple string transformations or condition counting on string columns, compute them on unique values and apply via `.map()` rather than applying them across the entire column.
