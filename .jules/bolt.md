## 2024-05-24 - Pandas loop allocation
**Learning:** Iteratively filtering and reallocating DataFrames inside a loop causes significant memory and performance overhead.
**Action:** Compute a sequential boolean mask across iterations and apply it outside the loop to perform a single allocation.
