import time
import pandas as pd
import numpy as np

def run_test():
    # Larger dataset to see impact
    n = 1000000
    df = pd.DataFrame({
        'col1': np.random.normal(0, 1, n),
        'col2': np.random.normal(0, 1, n),
        'col3': np.random.normal(0, 1, n)
    })
    # add some outliers
    df.loc[0:1000, 'col1'] = 100
    df.loc[1001:2000, 'col2'] = 100

    # Original
    start = time.time()
    df1 = df.copy()
    outliers_removed1 = 0
    numeric_cols = df1.columns
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
    print(f"Outliers original: {time.time() - start}")

    # Opt 1
    start = time.time()
    df2 = df.copy()
    outliers_removed2 = 0
    numeric_cols = df2.columns

    mask = pd.Series(True, index=df2.index)
    for col in numeric_cols:
        # Calculate bounds on the valid subset!
        valid_series = df2.loc[mask, col]
        Q1, Q3 = np.nanpercentile(valid_series, [25, 75])
        IQR = Q3 - Q1
        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR

        # update mask - wait, does this match pd.quantile behavior? Yes.
        col_data = df2[col]
        # Ignore NaNs logically, just like pandas does, by using >= and <= which yield False for NaNs.
        mask &= (col_data >= lower) & (col_data <= upper)

    before = df2.shape[0]
    df2 = df2[mask]
    after = df2.shape[0]
    outliers_removed2 = before - after

    print(f"Outliers optimized 1: {time.time() - start}")

    # Check if they match
    print("Match:", df1.equals(df2))
    print("Outliers count match:", outliers_removed1 == outliers_removed2)


run_test()
