## 2025-02-06 - Pandas String Operations
**Learning:** Using `.str` accessors across entire pandas string columns is significantly slower than calculating `.value_counts()` and mapping the operations across the unique values for columns with many repeated values.
**Action:** Use `value_counts()` and a dictionary mapping approach to optimize pandas string manipulations when appropriate.
