import time
import pandas as pd
import numpy as np

# Let's test with the actual dataset but repeated to make it larger
df_base = pd.read_csv("crime dataset.csv")
# repeat it 50 times
df = pd.concat([df_base]*50, ignore_index=True)
df.columns = df.columns.str.lower().str.strip().str.replace(" ", "_")
df = df.loc[:, ~df.columns.duplicated()]
df = df.convert_dtypes()
num_cols = df.select_dtypes(include=['int64', 'Int64', 'float64']).columns
df[num_cols] = df[num_cols].astype(float)
df[num_cols] = df[num_cols].fillna(df[num_cols].mean())

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
