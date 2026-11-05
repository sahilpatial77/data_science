import time
import pandas as pd
import numpy as np

n = 5000000
df = pd.DataFrame({
    'col1': np.random.normal(0, 1, n),
    'col2': np.random.normal(0, 1, n),
    'col3': np.random.normal(0, 1, n),
    'col4': np.random.normal(0, 1, n),
    'col5': np.random.normal(0, 1, n),
    'col6': np.random.normal(0, 1, n),
    'col7': np.random.normal(0, 1, n),
    'col8': np.random.normal(0, 1, n),
})
df.loc[0:500, 'col1'] = np.nan
df.loc[501:1000, 'col2'] = np.nan

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
df3 = df.copy()
numeric_cols = df3.select_dtypes(include=['float64']).columns
mask = pd.Series(True, index=df3.index)
for col in numeric_cols:
    # use np.nanpercentile which correctly skips nans like pd.quantile
    Q1, Q3 = np.nanpercentile(df3.loc[mask, col], [25, 75])
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    mask &= (df3[col] >= lower) & (df3[col] <= upper)
df3 = df3[mask]
print(f"Mask + numpy.nanpercentile: {time.time() - start}")

print(df1.equals(df3))
