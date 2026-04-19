import pandas as pd
import numpy as np
import time

np.random.seed(42)
df_orig = pd.DataFrame({
    'A': np.random.randn(100000),
    'B': np.random.randn(100000),
    'C': np.random.randn(100000),
    'D': np.random.randn(100000)
})

# Add some outliers
df_orig.loc[0, 'A'] = 100
df_orig.loc[1, 'B'] = 100
df_orig.loc[2, 'C'] = 100
df_orig.loc[3, 'D'] = 100

# Original
df1 = df_orig.copy()
start = time.time()
numeric_cols = df1.select_dtypes(include=['float64']).columns
outliers_removed1 = 0
for col in numeric_cols:
    Q1 = df1[col].quantile(0.25)
    Q3 = df1[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    before = df1.shape[0]
    df1 = df1[(df1[col] >= lower) & (df1[col] <= upper)]
    after = df1.shape[0]
    outliers_removed1 += (before - after)
time1 = time.time() - start

# Optimized
df2 = df_orig.copy()
start = time.time()
numeric_cols = df2.select_dtypes(include=['float64']).columns
outliers_removed2 = 0
mask = pd.Series(True, index=df2.index)
for col in numeric_cols:
    Q1 = df2.loc[mask, col].quantile(0.25)
    Q3 = df2.loc[mask, col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    before = mask.sum()
    mask = mask & (df2[col] >= lower) & (df2[col] <= upper)
    after = mask.sum()
    outliers_removed2 += (before - after)
df2 = df2[mask]
time2 = time.time() - start

print(f"Original: {outliers_removed1} removed, Time: {time1:.4f}s")
print(f"Optimized: {outliers_removed2} removed, Time: {time2:.4f}s")
print("DataFrames equal:", df1.equals(df2))
