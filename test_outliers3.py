import time
import pandas as pd
import numpy as np

# Use the exact logic from the codebase but applied to a large dataset
n = 1000000
df = pd.DataFrame({
    'col1': np.random.normal(0, 1, n),
    'col2': np.random.normal(0, 1, n),
    'col3': np.random.normal(0, 1, n)
})
df.loc[0:1000, 'col1'] = 100

start = time.time()
df1 = df.copy()
numeric_cols = df1.select_dtypes(include=['float64']).columns
for col in numeric_cols:
    Q1 = df1[col].quantile(0.25)
    Q3 = df1[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    df1 = df1[(df1[col] >= lower) & (df1[col] <= upper)]
print(f"Original Outlier Removal: {time.time() - start}")

start = time.time()
df2 = df.copy()
numeric_cols = df2.select_dtypes(include=['float64']).columns
mask = pd.Series(True, index=df2.index)
for col in numeric_cols:
    valid_series = df2.loc[mask, col]
    Q1 = valid_series.quantile(0.25)
    Q3 = valid_series.quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    mask &= (df2[col] >= lower) & (df2[col] <= upper)
df2 = df2[mask]
print(f"Optimized Outlier Removal: {time.time() - start}")
print(df1.equals(df2))
