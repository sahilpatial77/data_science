import time
import pandas as pd
import numpy as np

def run_test():
    df = pd.read_csv("crime dataset.csv")
    df.columns = df.columns.str.lower().str.strip().str.replace(" ", "_")
    df = df.loc[:, ~df.columns.duplicated()]
    df = df.convert_dtypes()

    # Original
    start = time.time()
    df1 = df.copy()
    outliers_removed = 0
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
        outliers_removed += (before - after)
    print(f"Outliers original: {time.time() - start}")

    # Opt 1
    start = time.time()
    df2 = df.copy()
    outliers_removed = 0
    numeric_cols = df2.select_dtypes(include=['float64']).columns

    mask = pd.Series(True, index=df2.index)
    for col in numeric_cols:
        # Calculate bounds on the valid subset!
        valid_series = df2.loc[mask, col]
        # using np.nanpercentile is faster than pd.quantile for non-NaN arrays, but here we may have NaNs. Wait, pd.quantile handles NaNs.
        Q1 = valid_series.quantile(0.25)
        Q3 = valid_series.quantile(0.75)
        IQR = Q3 - Q1
        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR

        # update mask
        mask &= (df2[col] >= lower) & (df2[col] <= upper)

    before = df2.shape[0]
    df2 = df2[mask]
    after = df2.shape[0]
    outliers_removed = before - after

    print(f"Outliers optimized 1: {time.time() - start}")


run_test()
