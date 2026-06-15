## 2024-05-01 - [Title]
**Learning:** [Insight]
**Action:** [How to apply next time]

## 2024-05-01 - [Optimize Pandas Outlier Removal]
**Learning:** Sequential outlier removal via dataframe filtering (`df = df[(df[col] >= lower) & (df[col] <= upper)]`) inside a loop over numeric columns is an O(N) memory allocation problem per column, leading to significant overhead for large dataframes.
**Action:** Accumulate outlier mask cumulatively (`mask &= ...`) and calculate quantiles on the continuously masked data (`df.loc[mask, col].quantile()`) rather than re-creating the entire DataFrame at each step. This significantly reduces computation time.

## 2024-05-01 - [Avoid O(N) iteration over `.isnull().sum()`]
**Learning:** `df.isnull().sum() > 0` iterates the full column, calculating the full sum before checking if it is greater than zero.
**Action:** Use `.any()` or `.hasnans` instead, which short-circuits.
