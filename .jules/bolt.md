## 2025-01-08 - Optimize pandas string formatting using dictionary mapping
**Learning:** Applying string methods like `.str.strip()` and `.str.lower()` across entire pandas columns is unnecessarily slow when dealing with highly repetitive categorical data.
**Action:** Use `.unique()` or `.value_counts()` to compute string transformations only on unique elements, then apply the results using a dictionary `.map()` to achieve significant speedups.
