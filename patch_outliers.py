import re

with open('main.py', 'r') as f:
    content = f.read()

original = """outliers_removed = 0

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

    outliers_removed += (before - after)"""

optimized = """outliers_removed = 0

numeric_cols = df.select_dtypes(include=['float64']).columns

mask = pd.Series(True, index=df.index)
for col in numeric_cols:
    # Use np.nanpercentile for faster quantile calculation
    Q1, Q3 = np.nanpercentile(df.loc[mask, col], [25, 75])
    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    # Maintain sequential boolean mask instead of repeated DataFrame reallocation
    mask &= (df[col] >= lower) & (df[col] <= upper)

before = df.shape[0]
df = df[mask]
after = df.shape[0]

outliers_removed = before - after"""

if original in content:
    content = content.replace(original, optimized)
    with open('main.py', 'w') as f:
        f.write(content)
    print("Replaced successfully")
else:
    print("Could not find original block")
