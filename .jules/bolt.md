## 2026-09-05 - String Column Optimization
**Learning:** Computing transformations on .unique() values using a pure Python dictionary and applying them via .map() is significantly faster than using sequential .str accessor methods over entire large pandas DataFrame columns.
**Action:** Apply dictionary mapping on unique values instead of vectorised string methods for cleaning repeating string columns.
