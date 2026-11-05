import time
import pandas as pd

n = 1000000
df = pd.DataFrame({
    'date_rptd': pd.date_range(start='2020-01-01', periods=n, freq='s').astype(str),
    'date_occ': pd.date_range(start='2020-01-01', periods=n, freq='s').astype(str)
})

date_cols = ["date_rptd", "date_occ"]

# Original
start = time.time()
df1 = df.copy()
for c in date_cols:
    df1[c] = pd.to_datetime(df1[c], errors="coerce")
print(f"Original: {time.time() - start}")

# Optimized
start = time.time()
df2 = df.copy()
for c in date_cols:
    if c in df2.columns:
        df2[c] = pd.to_datetime(df2[c], format='mixed', errors="coerce")
print(f"Optimized format mixed: {time.time() - start}")

print(df1.equals(df2))
