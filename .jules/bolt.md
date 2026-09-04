## 2024-09-04 - Optimize pandas string operations using dictionary mapping
**Learning:** Sequential `.str` operations over large pandas columns with repeating values are significantly slower than calculating operations on `.unique()` items via dictionary mapping and applying them via `.map()`. Vectorizing over entire categorical-like data can be highly inefficient in Python compared to single mapping lookups.
**Action:** Use `.map()` with a pre-computed dictionary of transformations when standardizing string columns that contain many repeating values.
