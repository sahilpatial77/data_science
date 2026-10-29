## 2023-10-24 - Repeated DataFrame Allocations
**Learning:** Repeatedly filtering and reallocating DataFrames inside a loop causes significant memory and performance overhead.
**Action:** Compute a sequential boolean mask across iterations and apply it once outside the loop. Use loc on the mask for dependent statistics.
