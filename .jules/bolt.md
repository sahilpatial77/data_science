## 2024-07-27 - [Sequential Pandas Filtering]
**Learning:** Sequential filtering in loops causes N intermediate allocations (where N is columns). When removing outliers iteratively, calculating quantiles and applying filters in-place allocates new DataFrames continuously.
**Action:** Use a boolean `mask` updated recursively `mask &= new_condition`, calculating quantiles dynamically on `df.loc[mask, col]`. Apply mask once at the end to save allocations while preserving exact logic.
