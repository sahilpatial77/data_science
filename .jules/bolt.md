## 2024-05-24 - Pandas Date Parsing Performance
**Learning:** Relying on pandas to infer datetime formats using `pd.to_datetime` with `format='mixed'` or without a format string causes massive performance degradation on large datasets, as it infers format per row instead of utilizing optimized vectorized C operations.
**Action:** Always explicitly specify the exact datetime string format (e.g., `format='%m/%d/%Y %I:%M:%S %p'`) when calling `pd.to_datetime` for a massive (roughly 19x) speed improvement.
