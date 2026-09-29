## 2023-10-24 - Pandas String Optimization and Date Parsing
**Learning:** Using vectorized `.str` methods on Pandas columns with low cardinality is significantly slower than iterating over `.value_counts()` and applying a `.map()` dictionary. Additionally, specifying `format` in `pd.to_datetime` vastly improves parsing speed by skipping format inference.
**Action:** Always optimize data transformation by utilizing dictionary mappings and explicit datetime formats when applicable.
