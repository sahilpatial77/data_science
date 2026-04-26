import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': [1, 2, 3, 4, 100],
    'B': [1, 2, 3, 4, 100]
})

print("Original shape:", df.shape)

# Original way
df1 = df.copy()
numeric_cols = df1.select_dtypes(include=['float64', 'int64']).columns
for col in numeric_cols:
    Q1 = df1[col].quantile(0.25)
    Q3 = df1[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    df1 = df1[(df1[col] >= lower) & (df1[col] <= upper)]
print("Original final shape:", df1.shape)
print(df1)

# Optimized way
df2 = df.copy()
mask = pd.Series(True, index=df2.index)
for col in numeric_cols:
    masked_col = df2.loc[mask, col]
    Q1 = masked_col.quantile(0.25)
    Q3 = masked_col.quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    mask = mask & (df2[col] >= lower) & (df2[col] <= upper)

df2 = df2[mask]
print("Optimized final shape:", df2.shape)
print(df2)
