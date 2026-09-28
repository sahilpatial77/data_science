## 2023-10-24 - Pandas String Optimization
**Learning:** Replacing sequential vectorized pandas string operations (like `.str.strip()`) with a Python dictionary mapping generated over `.value_counts()` is vastly superior for low-cardinality data, improving parsing speed by ~4.5x, but introduces edge cases for `pd.NA` mapping which require explicit handling.
**Action:** Use value_counts() mapping for repeated string standardization on dataset features, but remember to explicitly check for `isinstance(val, str)` and append `.astype('string')`.
