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
    space_count = 0
    for col in df1.select_dtypes(include='string'):
        space_count += df1[col].str.startswith(" ").sum()
        space_count += df1[col].str.endswith(" ").sum()
        df1[col] = df1[col].str.strip()
        df1[col] = df1[col].str.lower()
        df1[col] = df1[col].replace("", pd.NA)
    print(f"String clean original: {time.time() - start}")

    # Opt 1
    start = time.time()
    df2 = df.copy()
    space_count = 0
    string_cols = df2.select_dtypes(include='string').columns
    for col in string_cols:
        series = df2[col]
        # Calculate spaces before modifying
        space_count += (series.str.startswith(" ") | series.str.endswith(" ")).sum()
        # Combine strip and lower
        df2[col] = series.str.strip().str.lower().replace("", pd.NA)
    print(f"String clean optimized 1: {time.time() - start}")


run_test()
