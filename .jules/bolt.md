## 2024-09-05 - Optimized String Operations using Unique Dictionary Mapping
**Learning:** Sequential `.str` operations in pandas on large repeating string datasets create massive overhead, but pure dictionary mapping of `.unique()` values avoids repeating transformations on duplicates.
**Action:** Use `.unique()` and dictionary mapping instead of `.str` operations over the entire column.
