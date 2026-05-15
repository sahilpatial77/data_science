## 2024-05-19 - Pandas Optimization
**Learning:** When evaluating performance improvements using `pandas`, the development environment might lack `pandas` preventing benchmarking. In such cases, if performance impact cannot be measured due to environmental constraints, PRs must explicitly document why measurement was impractical and provide a technical rationale for the improvement.
**Action:** Proceed with performance PRs if there is strong theoretical justification (e.g. O(N) memory allocations in loops), but explicitly document the measurement constraints.
