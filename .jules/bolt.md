## 2024-07-27 - Optimizing Sequential DataFrame Filtering
**Learning:** Sequential DataFrame filtering inside loops (e.g., df = df[...]) causes expensive O(N) memory allocations, a specific performance anti-pattern in pandas data science scripts.
**Action:** Use a cumulative boolean mask (mask &= ...) to track filtering conditions dynamically, and apply the final mask once outside the loop.