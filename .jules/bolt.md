## 2024-05-15 - Optimizing Pandas Date Parsing
**Learning:** Specifying a strict date format in pd.to_datetime when format is known skips pandas' slow format inference step, yielding up to a 20x parsing speedup. Also, converting Series types rather than looping over individual string operations saves unnecessary overhead.
**Action:** Always define the format string in pd.to_datetime when working with standardized timestamp structures, and prefer vectorized string operations directly on entire DataFrame columns where applicable.
