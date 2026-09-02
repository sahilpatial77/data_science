## 2024-07-27 - Pandas String Operations Optimization
**Learning:** Repeated pandas .str operations (e.g., .str.startswith, .str.strip, .str.lower) on large string columns evaluate every row multiple times, causing a performance bottleneck. Computing transformations once per unique value via .value_counts() and applying them using .map() is significantly faster.
**Action:** When cleaning large categorical string columns in Pandas, use a dictionary map generated from unique values rather than applying multiple sequential .str methods across the entire series.
