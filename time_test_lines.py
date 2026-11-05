import time
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

def run_test():
    start = time.time()
    df = pd.read_csv("crime dataset.csv")
    print(f"Load time: {time.time() - start}")

    start = time.time()
    df.columns = df.columns.str.lower().str.strip().str.replace(" ", "_")
    df = df.loc[:, ~df.columns.duplicated()]
    df = df.convert_dtypes()
    print(f"Clean columns and types time: {time.time() - start}")

    start = time.time()
    space_count = 0
    for col in df.select_dtypes(include='string'):
        space_count += df[col].str.startswith(" ").sum()
        space_count += df[col].str.endswith(" ").sum()
        df[col] = df[col].str.strip()
        df[col] = df[col].str.lower()
        df[col] = df[col].replace("", pd.NA)
    print(f"String clean time: {time.time() - start}")

    start = time.time()
    num_cols = df.select_dtypes(include=['int64', 'Int64', 'float64']).columns
    df[num_cols] = df[num_cols].astype(float)
    df[num_cols] = df[num_cols].fillna(df[num_cols].mean())
    for col in df.select_dtypes(include='string'):
        if df[col].isnull().sum() > 0:
            df[col] = df[col].fillna(df[col].mode()[0])
    df = df.drop_duplicates()
    print(f"Missing values & duplicates time: {time.time() - start}")

    start = time.time()
    date_cols = ["date_rptd", "date_occ"]
    for c in date_cols:
        if c in df.columns:
            df[c] = pd.to_datetime(df[c], errors="coerce")
    print(f"Date parsing time: {time.time() - start}")

    start = time.time()
    if "vict_age" in df.columns:
        df = df[df["vict_age"] >= 0]
    if "lat" in df.columns and "lon" in df.columns:
        df = df[(df["lat"].between(-90, 90)) & (df["lon"].between(-180, 180))]
    print(f"Invalid values time: {time.time() - start}")

    start = time.time()
    numeric_cols = df.select_dtypes(include=['float64']).columns
    for col in numeric_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR
        df = df[(df[col] >= lower) & (df[col] <= upper)]
    print(f"Outliers time: {time.time() - start}")

    start = time.time()
    # Mocking stats and plots...
    if "vict_age" in df.columns:
        group1 = df["vict_age"].sample(frac=0.5, random_state=1)
        group2 = df["vict_age"].drop(group1.index)
        stats.ttest_ind(group1, group2)
        sample = df["vict_age"].sample(100, random_state=1)
        (sample.mean() - df["vict_age"].mean()) / (df["vict_age"].std() / np.sqrt(len(sample)))
    if "vict_age" in df.columns and "time_occ" in df.columns:
        stats.pearsonr(df["vict_age"], df["time_occ"])
    print(f"Stats time: {time.time() - start}")

    start = time.time()
    plt.figure(figsize=(10,7))
    num_df = df.select_dtypes(include=['float64'])
    if num_df.shape[1] >= 2:
        sns.heatmap(num_df.corr(), cmap="coolwarm")
        plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.close()

    if "vict_age" in df.columns:
        plt.figure()
        sns.histplot(df["vict_age"], bins=30)
        plt.title("Victim Age Distribution")
        plt.close()

    if "crm_cd_desc" in df.columns:
        plt.figure()
        top10 = df["crm_cd_desc"].value_counts().head(10)
        sns.barplot(x=top10.values, y=top10.index)
        plt.title("Top 10 Crimes")
        plt.close()

    if "date_occ" in df.columns:
        plt.figure()
        df_time = df[["date_occ"]].copy()
        df_time["month"] = df_time["date_occ"].dt.to_period("M").dt.to_timestamp()
        monthly = df_time.groupby("month").size()
        plt.plot(monthly.index, monthly.values)
        plt.title("Monthly Crimes")
        plt.xticks(rotation=45)
        plt.close()

    if "time_occ" in df.columns and "vict_age" in df.columns:
        plt.figure()
        sns.scatterplot(data=df, x="time_occ", y="vict_age", alpha=0.3)
        plt.title("Age vs Time")
        plt.close()
    print(f"Plot time: {time.time() - start}")

run_test()
