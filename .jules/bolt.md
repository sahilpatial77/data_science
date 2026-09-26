## 2024-05-18 - Optimize Pandas String Operations
**Learning:** In pandas data science scripts processing large datasets with repeating values, calculating `.value_counts()` and iterating in pure Python is significantly faster than applying `.str` accessors across the entire column.
**Action:** Use `.value_counts()` and `.map()` instead of `.str` accessors for bulk string operations on large datasets with low cardinality.
