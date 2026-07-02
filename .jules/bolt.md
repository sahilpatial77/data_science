## 2024-07-02 - O(N) DataFrame Filtering in Loops
**Learning:** Performing sequential boolean filtering on a Pandas DataFrame (`df = df[condition]`) within a loop creates a new copy of the DataFrame at each iteration, resulting in expensive O(N) memory allocations per loop cycle.
**Action:** Replace sequential filtering with a cumulative boolean mask (`mask &= condition`) and filter the DataFrame exactly once after the loop finishes.
