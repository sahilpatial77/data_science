## 2023-10-24 - Pandas Optimizations
**Learning:** pd.to_datetime without format string falls back to dateutil inference, which is highly inefficient. Chaining string methods is also slightly faster than individual allocations.
**Action:** Always provide explicit format='%m/%d/%Y %I:%M:%S %p' when known and chain string methods to avoid intermediate copies.
