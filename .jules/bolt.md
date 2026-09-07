## 2024-09-05 - Optimize string cleaning in Pandas
**Learning:** Sequential `.str` accessor methods like `.str.strip()` and `.str.lower()` in pandas loops run in O(N) time across entire string columns, creating a severe performance bottleneck on large datasets. Computing transformations on `.unique()` values using a pure Python dictionary and applying them via `.map()` is significantly faster (O(U)).
**Action:** Use `.unique()` and dictionary mapping for string operations on large columns with repeating values.
