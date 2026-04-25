# ================= FIX BACKEND =================
import matplotlib
matplotlib.use('TkAgg')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats


# ================= LOAD DATA =================
df = pd.read_csv("crime dataset.csv")


# ================= INITIAL REPORT =================
print("\n🔹 ORIGINAL SHAPE:", df.shape)
print("\n🔹 DUPLICATES:", df.duplicated().sum())
print("\n🔹 MISSING VALUES:\n", df.isnull().sum())


# ================= 1. CLEAN COLUMN NAMES =================
df.columns = df.columns.str.lower().str.strip().str.replace(" ", "_")


# ================= 2. REMOVE DUPLICATE COLUMNS =================
df = df.loc[:, ~df.columns.duplicated()]
print("\n🔹 Duplicate columns if any one is there in dataset")


# ================= 3. CONVERT TO MODERN DTYPES =================
df = df.convert_dtypes()


# ================= 4. CLEAN STRING DATA =================
space_count = 0

for col in df.select_dtypes(include='string'):
    space_count += df[col].str.startswith(" ").sum()
    space_count += df[col].str.endswith(" ").sum()

    df[col] = df[col].str.strip()                # remove spaces
    df[col] = df[col].str.lower()                # standardize text
    df[col] = df[col].replace("", pd.NA)

print("\n🔹 Spaces cleaned:", space_count)


# ================= 5. HANDLE MISSING VALUES =================
# numeric columns
num_cols = df.select_dtypes(include=['int64', 'Int64', 'float64']).columns
df[num_cols] = df[num_cols].astype(float)

missing_before = df.isnull().sum().sum()

df[num_cols] = df[num_cols].fillna(df[num_cols].mean())

# categorical
for col in df.select_dtypes(include='string'):
    if df[col].isnull().sum() > 0:
        df[col] = df[col].fillna(df[col].mode()[0])

missing_after = df.isnull().sum().sum()

print("\n🔹 Missing before:", missing_before)
print("🔹 Missing after:", missing_after)


# ================= 6. REMOVE DUPLICATES =================
df = df.drop_duplicates()
print("\n🔹 Shape after removing duplicates:", df.shape)


# ================= 7. FIX DATA TYPES =================
date_cols = ["date_rptd", "date_occ"]
invalid_dates = 0

for c in date_cols:
    if c in df.columns:
        before = df[c].isnull().sum()
        df[c] = pd.to_datetime(df[c], errors="coerce")
        after = df[c].isnull().sum()
        invalid_dates += (after - before)

print("\n🔹 Invalid dates:", invalid_dates)


# ================= 8. REMOVE INVALID VALUES =================
# remove negative ages
if "vict_age" in df.columns:
    invalid_age = (df["vict_age"] < 0).sum()
    df = df[df["vict_age"] >= 0]
    print("\n🔹 Negative ages removed:", invalid_age)

# remove invalid coordinates
if "lat" in df.columns and "lon" in df.columns:
    df = df[(df["lat"].between(-90, 90)) & (df["lon"].between(-180, 180))]
    print("🔹 Invalid coordinates removed")


# ================= 9. OUTLIER REMOVAL =================
# ⚡ BOLT OPTIMIZATION:
# Avoid O(N) DataFrame memory allocations by evaluating boolean masks cumulatively
# and computing quantiles on progressively masked data.
outliers_removed = 0

numeric_cols = df.select_dtypes(include=['float64']).columns
mask = pd.Series(True, index=df.index)

for col in numeric_cols:
    Q1 = df.loc[mask, col].quantile(0.25)
    Q3 = df.loc[mask, col].quantile(0.75)
    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    mask = mask & (df[col] >= lower) & (df[col] <= upper)

before_total = df.shape[0]
df = df[mask]
outliers_removed = before_total - df.shape[0]

print("\n🔹 Outliers removed:", outliers_removed)


# ================= 10. FINAL VALIDATION =================
print("\n🔹 FINAL shape of dataset :", df.shape)
print("\n🔹 FINAL missing values are there in dataset\n", df.isnull().sum())


# ================= SHOW FINAL CLEAN DATA =================
print("\n🔹 CLEANED DATASET:\n")
print(df.head(20))

print("\n🔹 CLEANED DATASET:\n")
print(df.tail(20))


# ================= OPTIONAL: FULL DATA DISPLAY =================
# WARNING: Only use if dataset is small
print(df)

print("\n================= STATISTICAL TESTING =================")

# ------------------ T-TEST ------------------
# Example: Compare victim age for two random groups
if "vict_age" in df.columns:
    
    # split dataset into 2 groups randomly
    group1 = df["vict_age"].sample(frac=0.5, random_state=1)
    group2 = df["vict_age"].drop(group1.index)

    t_stat, p_val = stats.ttest_ind(group1, group2)

    print("\n🔹 T-TEST (Victim Age Comparison)")
    print("T-Statistic:", t_stat)
    print("P-Value:", p_val)

    if p_val < 0.05:
        print("Result: Significant difference between groups")
    else:
        print("Result: No significant difference")


# ------------------ Z-TEST ------------------
# comparing sample mean with population mean
if "vict_age" in df.columns:

    sample = df["vict_age"].sample(100, random_state=1)
    sample_mean = sample.mean()
    population_mean = df["vict_age"].mean()
    std = df["vict_age"].std()

    z_score = (sample_mean - population_mean) / (std / np.sqrt(len(sample)))

    print("\n🔹 Z-TEST (Sample vs Population)")
    print("Z-Score:", z_score)

    if abs(z_score) > 1.96:
        print("Result: Significant difference (95% confidence)")
    else:
        print("Result: No significant difference")


# ------------------ CORRELATION TEST ------------------
if "vict_age" in df.columns and "time_occ" in df.columns:

    corr, p_val = stats.pearsonr(df["vict_age"], df["time_occ"])

    print("\n🔹 CORRELATION TEST (Age vs Time)")
    print("Correlation:", corr)
    print("P-Value:", p_val)

    if p_val < 0.05:
        print("Result: Significant correlation")
    else:
        print("Result: No significant correlation")


# ================= (1) HEATMAP =================
plt.figure(figsize=(10,7))
num_df = df.select_dtypes(include=['float64'])

if num_df.shape[1] >= 2:
    sns.heatmap(num_df.corr(), cmap="coolwarm")
    plt.title("Correlation Heatmap")

plt.tight_layout()
plt.show()
plt.close()


# ================= (2) HISTOGRAM =================
if "vict_age" in df.columns:
    plt.figure()
    sns.histplot(df["vict_age"], bins=30)
    plt.title("Victim Age Distribution")
    plt.show()
    plt.close()


# ================= (3) BAR =================
if "crm_cd_desc" in df.columns:
    plt.figure()
    top10 = df["crm_cd_desc"].value_counts().head(10)
    sns.barplot(x=top10.values, y=top10.index)
    plt.title("Top 10 Crimes")
    plt.show()
    plt.close()


# ================= (4) LINE =================
if "date_occ" in df.columns:
    plt.figure()
    df_time = df[["date_occ"]].copy()
    df_time["month"] = df_time["date_occ"].dt.to_period("M").dt.to_timestamp()

    monthly = df_time.groupby("month").size()

    plt.plot(monthly.index, monthly.values)
    plt.title("Monthly Crimes")
    plt.xticks(rotation=45)
    plt.show()
    plt.close()


# ================= (5) SCATTER =================
if "time_occ" in df.columns and "vict_age" in df.columns:
    plt.figure()
    sns.scatterplot(data=df, x="time_occ", y="vict_age", alpha=0.3)
    plt.title("Age vs Time")
    plt.show()
    plt.close()






