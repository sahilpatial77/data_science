## 2026-11-03 - Avoid DataFrame reallocation in loops
**Learning:** Repeatedly filtering and reallocating DataFrames inside a loop causes significant memory and performance overhead.
**Action:** Compute a sequential boolean mask across iterations (e.g., mask &= ...) and apply it outside the loop to perform a single allocation. Ensure dependent statistics (like quantiles) use the mask to maintain mathematical correctness.
