import time
import pandas as pd

n = 1000000
df = pd.DataFrame({
    'col1': [" a ", "b", " c", "d "] * (n // 4),
    'col2': [" A ", "B", " C", "D "] * (n // 4),
})
df = df.astype("string")

# Original
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

# Optimized
start = time.time()
df2 = df.copy()
space_count = 0
for col in df2.columns:
    series = df2[col]
    space_count += (series.str.startswith(" ") | series.str.endswith(" ")).sum()
    df2[col] = series.str.strip().str.lower().replace("", pd.NA)
print(f"Optimized string clean: {time.time() - start}")

print(df1.equals(df2))
