## 2024-11-20 - Sequential Boolean Masks
**Learning:** Iteratively filtering and reallocating DataFrames inside a loop (e.g., `df = df[...]`) creates massive memory overhead and slows down data processing. It's a common anti-pattern in pandas data cleaning.
**Action:** Use a sequential boolean mask (e.g., `mask &= ...`) across iterations and apply the mask outside the loop (e.g., `df = df[mask]`) to perform a single allocation.
