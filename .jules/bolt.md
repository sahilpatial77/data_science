## 2024-10-17 - Optimize Pandas to_datetime
**Learning:** In Pandas, format inference during pd.to_datetime can be an extreme performance bottleneck. On this dataset, explicitly specifying the exact format strings yielded a ~20x speedup.
**Action:** Always specify the format parameter when using pd.to_datetime if the string format is known, avoiding 'mixed' format if possible.
