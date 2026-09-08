## 2024-09-08 - String Series Optimization
**Learning:** Sequential .str accessor methods over large pandas DataFrames with repeating values are a significant performance bottleneck because they process the entire column for every operation.
**Action:** Optimize string operations by mapping transformations over .unique() values or computing aggregates with .value_counts() using pure Python dictionaries, then apply them via .map().
