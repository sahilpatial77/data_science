## 2024-09-17 - Pandas String Operations Performance
**Learning:** Sequential `.str` operations on pandas DataFrames with repeating values are a significant performance bottleneck due to missing vectorization over duplicate elements.
**Action:** Optimize iterative string operations (like counting and stripping) by using `.value_counts()` and applying transformations on a `.map()` dictionary, which drastically reduces execution time.
