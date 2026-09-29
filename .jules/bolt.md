## 2024-05-15 - Fast pd.to_datetime formatting
**Learning:** In Pandas, passing a format explicitly instead of letting Pandas infer the datetime string bypasses the inferring overhead and results in much faster operations. Using dict mappings on repetitive duplicated values over the built in C-level string operations is a well-known anti-pattern and results in performance degradation despite the logic seemingly being an O(n) hashmap mapping.
**Action:** Use specific formats to pd.to_datetime and avoid mapping string elements.
