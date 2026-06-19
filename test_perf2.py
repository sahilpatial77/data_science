import pandas as pd
import numpy as np
import time

np.random.seed(42)
n_rows = 500000
df = pd.DataFrame({
    'col1': np.random.randn(n_rows),
    'col2': np.random.randn(n_rows),
    'col3': np.random.randn(n_rows),
})

# Sequential
df_seq = df.copy()
start_seq = time.time()
outliers_removed_seq = 0
for col in df_seq.columns:
    Q1 = df_seq[col].quantile(0.25)
    Q3 = df_seq[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    before = df_seq.shape[0]
    df_seq = df_seq[(df_seq[col] >= lower) & (df_seq[col] <= upper)]
    after = df_seq.shape[0]
    outliers_removed_seq += (before - after)
time_seq = time.time() - start_seq

# Cumulative Mask
df_cum = df.copy()
start_cum = time.time()
mask = pd.Series(True, index=df_cum.index)
for col in df_cum.columns:
    col_data = df_cum.loc[mask, col]
    Q1 = col_data.quantile(0.25)
    Q3 = col_data.quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    mask &= (df_cum[col] >= lower) & (df_cum[col] <= upper)
before = df_cum.shape[0]
df_cum = df_cum[mask]
after = df_cum.shape[0]
outliers_removed_cum = before - after
time_cum = time.time() - start_cum

print(f"Sequential: {time_seq:.4f}s")
print(f"Cumulative: {time_cum:.4f}s")
print(f"Match shape: {df_seq.shape} vs {df_cum.shape}")
print(f"Match removed: {outliers_removed_seq} vs {outliers_removed_cum}")
