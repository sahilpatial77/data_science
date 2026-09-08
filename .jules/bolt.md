## 2024-09-05 - Pandas String Operations
**Learning:** When operating on large pandas DataFrames with repeating values, computing string transformations on unique values using a dictionary and mapping them back is significantly faster than using sequential .str accessor methods over entire columns.
**Action:** In future Pandas optimizations, replace chained .str operations with .map() on unique values when dealing with categorical or highly repetitive text data.
