## 2023-10-24 - Pandas Outlier Removal Optimization
**Learning:** Iteratively modifying and reallocating a Pandas DataFrame inside a loop introduces massive overhead. In data cleaning scripts, this is a common anti-pattern.
**Action:** Use sequential boolean masking computed iteratively, and apply the final mask in a single allocation outside the loop.
