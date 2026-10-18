## 2023-10-24 - Pandas to_datetime Optimization
**Learning:** Pandas pd.to_datetime falls back to slow dateutil parsing when inferring formats, causing a major bottleneck in data ingestion.
**Action:** Always explicitly specify the format parameter to bypass inference.
