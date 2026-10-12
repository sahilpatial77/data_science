## 2024-10-12 - Optimize DateTime Parsing
**Learning:** Relying on Pandas internal format inference for datetime strings across multiple columns causes a significant bottleneck. Providing an explicit format string is strictly required for optimal performance on this codebase.
**Action:** Always specify the exact datetime format (e.g., format='%m/%d/%Y %I:%M:%S %p') when using pd.to_datetime unless dates are genuinely mixed format.
