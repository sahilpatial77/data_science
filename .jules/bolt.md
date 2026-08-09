## 2024-07-27 - [Pandas Sequential Filtering in Loops]
**Learning:** Sequential DataFrame filtering inside loops causes expensive O(N) memory allocations and slows down processing.
**Action:** Use a cumulative boolean mask to perform filtering in a single step at the end of the loop, updating intermediate state using the mask dynamically.
