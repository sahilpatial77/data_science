## 2023-10-24 - Pandas Loop Reallocation Overhead
**Learning:** Repeatedly filtering and reallocating DataFrames inside a loop (e.g., df = df[...]) causes significant memory overhead and creates multiple copies.
**Action:** Instead, compute a sequential boolean mask across iterations (e.g., mask &= ...) and apply it once outside the loop (e.g., df = df[mask]) to perform a single allocation.
