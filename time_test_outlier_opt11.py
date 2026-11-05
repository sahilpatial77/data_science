import time
import pandas as pd
import numpy as np

n = 5000000
df = pd.DataFrame({
    'col1': np.random.normal(0, 1, n),
    'col2': np.random.normal(0, 1, n),
    'col3': np.random.normal(0, 1, n),
    'col4': np.random.normal(0, 1, n),
    'col5': np.random.normal(0, 1, n),
    'col6': np.random.normal(0, 1, n),
    'col7': np.random.normal(0, 1, n),
    'col8': np.random.normal(0, 1, n),
})

start = time.time()
df3 = df.copy()
numeric_cols = df3.select_dtypes(include=['float64']).columns
mask = pd.Series(True, index=df3.index)
for col in numeric_cols:
    Q1, Q3 = np.nanpercentile(df3.loc[mask, col], [25, 75])
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    mask &= (df3[col] >= lower) & (df3[col] <= upper)
df3 = df3[mask]
print(f"Mask + numpy.nanpercentile: {time.time() - start}")
