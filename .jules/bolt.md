## 2024-09-10 - O(N) String Operations on Low Cardinality Data
**Learning:** Applying pandas .str accessors directly to entire columns with high duplication rates is a significant performance anti-pattern, resulting in redundant O(N) operations on the same string values.
**Action:** Use .unique() to extract unique values, process them purely in Python via a dictionary, and reapply using .map() to reduce complexity to O(K) where K is the number of unique strings.
