## 2024-05-24 - Optimize Pandas String Column Transformations
**Learning:** When optimizing string operations on large pandas DataFrames with repeating values, computing transformations on .unique() values using a pure Python dictionary and applying them via .map() is significantly faster than using sequential .str accessor methods over entire columns.
**Action:** Apply map-based optimizations for string operations on columns with low cardinality to avoid redundant computations.
