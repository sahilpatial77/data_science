## 2024-05-20 - pd.to_datetime Optimization
**Learning:** In Pandas, parsing strings to datetimes without an explicit format argument forces it to infer the format for each element, leading to slow performance.
**Action:** Always provide the exact datetime format to `pd.to_datetime(..., format='...')` to improve parsing speed by ~20x.
