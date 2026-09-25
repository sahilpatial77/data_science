## 2024-05-24 - Pandas String Optimization
**Learning:** Applying string methods like `.str.strip()` across an entire pandas column is slow when there are many duplicate strings. Using `value_counts()` and a dictionary mapping with `.map()` is significantly faster.
**Action:** Use dictionary mapping for pandas string cleaning when dealing with repetitive categorical text data.
