## 2024-09-12 - Vectorizing Pandas String Operations
**Learning:** Sequential `.str` accessor methods (like `.str.strip()`) applied directly to entire columns in pandas are highly inefficient for categorical-like text data due to redundant processing of identical strings.
**Action:** Use a dictionary mapping based on `.value_counts()` or `.unique()` to pre-compute transformations only on unique strings, then apply them in a single pass via `.map()`. This drastically reduces string operation overhead.
