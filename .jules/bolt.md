## 2024-05-24 - Avoid DataFrame Reallocations in Iterative Filtering
**Learning:** Repeatedly filtering and reallocating DataFrames inside a loop causes significant memory and performance overhead.
**Action:** Use boolean mask accumulation and apply it outside the loop.
