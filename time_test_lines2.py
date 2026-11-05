import time
import pandas as pd

def run_test():
    df = pd.read_csv("crime dataset.csv")

    date_cols = ["date_rptd", "date_occ"]

    start = time.time()
    for c in date_cols:
        if c in df.columns:
            df[c] = pd.to_datetime(df[c], errors="coerce")
    print(f"Date parsing default: {time.time() - start}")

    df = pd.read_csv("crime dataset.csv")

    start = time.time()
    for c in date_cols:
        if c in df.columns:
            # Try to infer format from first non-null
            idx = df[c].first_valid_index()
            if idx is not None:
                val = df.loc[idx, c]
                try:
                    fmt = None
                    if isinstance(val, str) and '-' in val:
                        # naive check
                        fmt = "%Y-%m-%d %H:%M:%S"
                        pd.to_datetime(val, format=fmt)
                        df[c] = pd.to_datetime(df[c], format=fmt, errors="coerce")
                    else:
                         df[c] = pd.to_datetime(df[c], errors="coerce")
                except ValueError:
                    df[c] = pd.to_datetime(df[c], errors="coerce")
            else:
                df[c] = pd.to_datetime(df[c], errors="coerce")

    print(f"Date parsing optimized: {time.time() - start}")


run_test()
