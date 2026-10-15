## 2023-10-24 - Pandas Datetime and Nullable String Optimizations
**Learning:** Specifying the datetime format in pandas `to_datetime` significantly improves parsing speed by skipping format inference. Also, when working with nullable string types, boolean masks may contain `pd.NA` which causes a ValueError when used for indexing.
**Action:** Always specify datetime formats explicitly when known, and explicitly handle `pd.NA` in boolean masks (e.g. using `.fillna(False)`) when performing conditional assignments on nullable columns.
