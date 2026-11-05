import time
import pandas as pd
import datetime

n = 100000
df = pd.DataFrame({
    'date_rptd': pd.date_range(start='2020-01-01', periods=n, freq='min').astype(str),
    'date_occ': pd.date_range(start='2020-01-01', periods=n, freq='min').astype(str)
})

# Original
start = time.time()
df1 = df.copy()
for c in df1.columns:
    df1[c] = pd.to_datetime(df1[c], errors="coerce")
print(f"Original to_datetime: {time.time() - start}")

# With format deduction
start = time.time()
df2 = df.copy()
for c in df2.columns:
    val = df2.loc[df2[c].first_valid_index(), c]
    try:
        pd.to_datetime(val, format="%Y-%m-%d %H:%M:%S", errors="raise")
        df2[c] = pd.to_datetime(df2[c], format="%Y-%m-%d %H:%M:%S", errors="coerce")
    except ValueError:
        df2[c] = pd.to_datetime(df2[c], errors="coerce")
print(f"Optimized to_datetime (deduced format): {time.time() - start}")

print(df1.equals(df2))
