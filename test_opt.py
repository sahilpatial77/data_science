import pandas as pd
import numpy as np

np.random.seed(42)
df_orig = pd.DataFrame({
    'date_rptd': ['2020-01-01', '2020-01-02'] * 50,
    'date_occ': ['2020-01-01', '2020-01-02'] * 50,
    'vict_age': np.random.randint(18, 60, 100).astype(float),
    'lat': np.random.uniform(33, 35, 100),
    'lon': np.random.uniform(-119, -117, 100),
    'crm_cd_desc': np.array(['Robbery', 'Burglary'] * 50).astype(str),
    'time_occ': np.random.randint(0, 2359, 100).astype(float)
})

df_orig.loc[10, 'vict_age'] = 9999
df_orig.loc[20, 'lat'] = 9999
df_orig.loc[30, 'lon'] = 9999
df_orig.loc[40, 'time_occ'] = 99999

df1 = df_orig.copy()

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

df2 = df_orig.copy()
outliers_removed2 = 0
numeric_cols = df2.select_dtypes(include=['float64']).columns
mask = pd.Series(True, index=df2.index)
for col in numeric_cols:
    active_subset = df2.loc[mask, col]
    Q1 = active_subset.quantile(0.25)
    Q3 = active_subset.quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    before = mask.sum()
    mask &= (df2[col] >= lower) & (df2[col] <= upper)
    after = mask.sum()
    outliers_removed2 += (before - after)
df2 = df2[mask]

print(f"Original logic: {outliers_removed1} outliers removed, shape {df1.shape}")
print(f"Optimized logic: {outliers_removed2} outliers removed, shape {df2.shape}")
assert df1.shape == df2.shape, "Shape mismatch"
assert outliers_removed1 == outliers_removed2, "Outliers removed mismatch"
print("SUCCESS!")
