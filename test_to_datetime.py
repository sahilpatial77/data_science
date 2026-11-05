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
        idx = df2[c].first_valid_index()
        if idx is not None:
            val = df2.loc[idx, c]
            if isinstance(val, str) and len(val) == 19 and val[10] == ' ':
                # Likely '%Y-%m-%d %H:%M:%S'
                try:
                    df2[c] = pd.to_datetime(df2[c], format="%Y-%m-%d %H:%M:%S", errors="coerce")
                except ValueError:
                    df2[c] = pd.to_datetime(df2[c], errors="coerce")
            else:
                df2[c] = pd.to_datetime(df2[c], errors="coerce")
print(f"Optimized format: {time.time() - start}")

print(df1.equals(df2))
