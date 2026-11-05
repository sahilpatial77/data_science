import time
import pandas as pd
import numpy as np

n = 1000000
df = pd.DataFrame({
    'col1': np.random.normal(0, 1, n),
    'col2': np.random.normal(0, 1, n),
    'col3': np.random.normal(0, 1, n)
})
df.loc[0:10000, 'col1'] = np.nan

start = time.time()
df1 = df.copy()
num_cols = df1.select_dtypes(include=['int64', 'Int64', 'float64']).columns
df1[num_cols] = df1[num_cols].astype(float)
df1[num_cols] = df1[num_cols].fillna(df1[num_cols].mean())
print(f"Original missing: {time.time() - start}")

start = time.time()
df2 = df.copy()
num_cols = df2.select_dtypes(include=['int64', 'Int64', 'float64']).columns
df2[num_cols] = df2[num_cols].astype(float)
# just use fillna without assigning all columns?
for col in num_cols:
    if df2[col].isna().any():
        df2[col] = df2[col].fillna(df2[col].mean())
print(f"Optimized missing: {time.time() - start}")
print(df1.equals(df2))
