## 2026-09-21 - Fast String Mapping in Pandas
**Learning:** When optimizing string operations on large pandas DataFrames with repeating values, computing transformations on .unique() values using a pure Python dictionary and applying them via .map() is significantly faster than using sequential .str accessor methods over entire columns.
**Action:** Extract unique values, build a transformation mapping dictionary, and apply using .map() to avoid repeating operations on duplicate strings.
