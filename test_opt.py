import pandas as pd
import numpy as np

# Generate data
np.random.seed(42)
df = pd.DataFrame({
    'vict_age': np.random.normal(50, 15, 1000),
    'lat': np.random.normal(34, 5, 1000),
    'lon': np.random.normal(-118, 5, 1000),
    'time_occ': np.random.normal(1200, 400, 1000)
})
df.loc[10, 'vict_age'] = 9999
df.loc[20, 'lat'] = 9999
df.loc[30, 'lon'] = 9999

df1 = df.copy()
df2 = df.copy()

# Original
outliers_removed1 = 0
numeric_cols = df1.select_dtypes(include=['float64']).columns
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

# Optimized
outliers_removed2 = 0
numeric_cols = df2.select_dtypes(include=['float64']).columns

# ⚡ Bolt: Use cumulative mask to prevent expensive O(N) sequential dataframe filtering allocations inside the loop
mask = pd.Series(True, index=df2.index)

for col in numeric_cols:
    active_col = df2.loc[mask, col]
    Q1 = active_col.quantile(0.25)
    Q3 = active_col.quantile(0.75)
    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    mask &= (df2[col] >= lower) & (df2[col] <= upper)

before_total = df2.shape[0]
df2 = df2[mask]
after_total = df2.shape[0]
outliers_removed2 = before_total - after_total

print("Original shape:", df1.shape)
print("Optimized shape:", df2.shape)
print("Original removed:", outliers_removed1)
print("Optimized removed:", outliers_removed2)
