import time
import pandas as pd
import numpy as np

df_base = pd.read_csv("crime dataset.csv")
df = pd.concat([df_base]*500, ignore_index=True)
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
df3 = df.copy()
numeric_cols = df3.select_dtypes(include=['float64']).columns
for col in numeric_cols:
    # Compute on df3[col], not valid_series
    Q1, Q3 = np.nanpercentile(df3[col], [25, 75])
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    df3 = df3[(df3[col] >= lower) & (df3[col] <= upper)]
print(f"Optimized Outlier Removal (no mask, just np): {time.time() - start}")

print(df1.equals(df3))
