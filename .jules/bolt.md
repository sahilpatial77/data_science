## 2024-05-20 - Outlier Removal Optimization
**Learning:** Replacing iterative DataFrame reallocations with a sequential boolean mask and numpy.nanpercentile reduces overhead.
**Action:** Apply sequential boolean masks for iterative filtering.
