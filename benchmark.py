import pandas as pd
import numpy as np
import time

# Create a large dataset
np.random.seed(42)
n_rows = 100000
df_orig = pd.DataFrame({
    'col1': np.random.randn(n_rows),
    'col2': np.random.randn(n_rows) * 10,
    'col3': np.random.randn(n_rows) * 100,
    'col4': np.random.randn(n_rows) * 1000,
})

def method_sequential(df):
    outliers_removed = 0
    numeric_cols = df.select_dtypes(include=['float64']).columns
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

def method_mask(df):
    outliers_removed = 0
    numeric_cols = df.select_dtypes(include=['float64']).columns
    mask = pd.Series(True, index=df.index)

    for col in numeric_cols:
        current_data = df.loc[mask, col]
        Q1 = current_data.quantile(0.25)
        Q3 = current_data.quantile(0.75)
        IQR = Q3 - Q1

        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR

        col_mask = (df[col] >= lower) & (df[col] <= upper)

        before = mask.sum()
        mask = mask & col_mask
        after = mask.sum()

        outliers_removed += (before - after)

    df = df[mask]
    return df, outliers_removed

# Warmup
_ = method_sequential(df_orig.copy())
_ = method_mask(df_orig.copy())

t0 = time.time()
df1, out1 = method_sequential(df_orig.copy())
t1 = time.time()

t2 = time.time()
df2, out2 = method_mask(df_orig.copy())
t3 = time.time()

print(f"Sequential: {t1-t0:.4f}s")
print(f"Mask: {t3-t2:.4f}s")
print(f"Outliers: {out1} vs {out2}")
print(f"Shape: {df1.shape} vs {df2.shape}")
