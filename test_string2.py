import time
import pandas as pd

n = 1000000
df = pd.DataFrame({
    'col1': [" a ", "b", " c", "d "] * (n // 4),
    'col2': [" A ", "B", " C", "D "] * (n // 4),
})
df = df.astype("string")

start = time.time()
df1 = df.copy()
space_count = 0
for col in df1.columns:
    space_count += df1[col].str.startswith(" ").sum()
    space_count += df1[col].str.endswith(" ").sum()
    df1[col] = df1[col].str.strip()
    df1[col] = df1[col].str.lower()
    df1[col] = df1[col].replace("", pd.NA)
print(f"Original string clean: {time.time() - start}")

start = time.time()
df2 = df.copy()
space_count2 = 0
for col in df2.columns:
    series = df2[col]
    # Actually just combining them doesn't do much. But wait, what if we use string methods properly?
    # No, string operations are already fairly optimized in pandas 2.0+ with pyarrow.
    space_count2 += series.str.startswith(" ").sum()
    space_count2 += series.str.endswith(" ").sum()
    df2[col] = series.str.strip().str.lower().replace("", pd.NA)
print(f"Optimized string clean: {time.time() - start}")
