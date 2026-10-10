## 2024-05-28 - Optimize pd.to_datetime parsing
**Learning:** When parsing dates in pandas across multiple columns, explicitly setting the format parameter (e.g., format='%m/%d/%Y %I:%M:%S %p') avoids expensive format inference and significantly speeds up parsing.
**Action:** Always specify the exact datetime format when using pd.to_datetime on large datasets to avoid ~20x performance drops.
