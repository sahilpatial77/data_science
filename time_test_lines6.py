import time
import pandas as pd
import numpy as np

def run_test():
    # Larger dataset to see impact
    n = 100000
    df = pd.DataFrame({
        'date_rptd': pd.date_range(start='2020-01-01', periods=n, freq='min'),
        'date_occ': pd.date_range(start='2020-01-01', periods=n, freq='min')
    })

    # Original
    start = time.time()
    df1 = df.copy()
    date_cols = ["date_rptd", "date_occ"]
    invalid_dates = 0
    for c in date_cols:
        if c in df1.columns:
            before = df1[c].isnull().sum()
            df1[c] = pd.to_datetime(df1[c], errors="coerce")
            after = df1[c].isnull().sum()
            invalid_dates += (after - before)
    print(f"Dates original: {time.time() - start}")

    # Opt 1
    start = time.time()
    df2 = df.copy()
    invalid_dates2 = 0
    for c in date_cols:
        if c in df2.columns:
            before = df2[c].isnull().sum()
            idx = df2[c].first_valid_index()
            if idx is not None:
                val = df2.loc[idx, c]
                try:
                    # Let's see if format infer works.
                    # if val is already timestamp, just coerce?
                    if isinstance(val, pd.Timestamp):
                        df2[c] = pd.to_datetime(df2[c], errors="coerce")
                    else:
                        df2[c] = pd.to_datetime(df2[c], errors="coerce") # not optimizing for now
                except ValueError:
                    df2[c] = pd.to_datetime(df2[c], errors="coerce")
            else:
                df2[c] = pd.to_datetime(df2[c], errors="coerce")
            after = df2[c].isnull().sum()
            invalid_dates2 += (after - before)
    print(f"Dates optimized: {time.time() - start}")

    # Opt 2 - real optimization
    # Instead of dates, let's optimize the outlier code which had some difference
run_test()
