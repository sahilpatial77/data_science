## 2024-09-14 - Optimize pandas string column operations
**Learning:** When computing aggregate string condition counts on large pandas DataFrames with repeating values, calculating .value_counts() and accumulating counts by iterating over unique values in pure Python is significantly faster than applying .str accessors across the entire column.
**Action:** Replace sequential .str accessor chains with .value_counts() and dictionary .map() for string normalization on columns with many duplicate values.
