## 2024-09-05 - [Initial Setup]
**Learning:** [Setting up the bolt journal]
**Action:** [No action needed]
## 2024-09-05 - Optimize string mapping in Pandas
**Learning:** Applying pandas string methods (like `.str.lower()` and `.str.strip()`) to an entire Series with many duplicates is inefficient, but extracting unique values via `value_counts()`, processing them in a pure Python dictionary, and applying the results via `.map()` is significantly faster for dataframes with highly repetitive strings.
**Action:** Opt for dictionary mapping over `.str` accessors on large Pandas columns with low cardinality.
