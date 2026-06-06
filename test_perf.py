import pandas as pd
import numpy as np
import time

# Create dummy data
np.random.seed(0)
df = pd.DataFrame({
    'A': np.random.randn(100000),
    'B': np.random.randn(100000),
    'C': np.random.randn(100000),
    'D': np.random.randn(100000)
})
df.loc[0, 'A'] = 100
df.loc[1, 'B'] = 100

def original_method(df):
    outliers_removed = 0
    numeric_cols = df.columns
    for col in numeric_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR
        before = df.shape[0]
        df = df[(df[col] >= lower) & (df[col] <= upper)]
        after = df.shape[0]
        outliers_removed += (before - after)
    return df, outliers_removed

def optimized_method(df):
    outliers_removed = 0
    numeric_cols = df.columns
    mask = pd.Series(True, index=df.index)

    for col in numeric_cols:
        valid_data = df.loc[mask, col]
        Q1 = valid_data.quantile(0.25)
        Q3 = valid_data.quantile(0.75)
        IQR = Q3 - Q1
        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR

        mask &= (df[col] >= lower) & (df[col] <= upper)

    before = df.shape[0]
    df = df[mask]
    after = df.shape[0]
    outliers_removed = before - after
    return df, outliers_removed

df1 = df.copy()
start = time.time()
res1, out1 = original_method(df1)
t1 = time.time() - start

df2 = df.copy()
start = time.time()
res2, out2 = optimized_method(df2)
t2 = time.time() - start

print("Original:", t1, "Outliers:", out1, "Shape:", res1.shape)
print("Optimized:", t2, "Outliers:", out2, "Shape:", res2.shape)
print("Are dataframes equal?", res1.equals(res2))
