## 2024-05-20 - Outlier Removal Boolean Mask
**Learning:** In pandas, iterative dataframe filtering (e.g. `df = df[...]`) inside loops causes unnecessary copying and is inefficient. Accumulating boolean masks (`mask &= col_mask`) and filtering once is much faster.
**Action:** Use boolean mask accumulation for multi-condition or multi-column dataframe filtering.
