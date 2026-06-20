## 2024-06-20 - Pandas Sequential Filtering Allocation Anti-Pattern
**Learning:** Sequential filtering in loops (`df = df[condition]`) is an extremely common anti-pattern in Pandas scripts that causes O(N*M) memory allocations and copies.
**Action:** Always replace sequential column-by-column filtering inside loops with a cumulative boolean mask (`mask = pd.Series(True, index=df.index)` -> `mask = mask & new_condition` -> `df = df[mask]`).
