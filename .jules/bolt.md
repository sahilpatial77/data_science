## 2026-05-02 - Pandas Cumulative Masking
**Learning:** Sequential DataFrame filtering in loops causes O(N) memory allocations. Switching to a simple cumulative boolean mask can change the underlying mathematical behavior if quantiles aren't progressively calculated.
**Action:** Evaluate boolean masks cumulatively and compute quantiles on the progressively masked data (e.g., `df.loc[mask, col]`) to avoid O(N) memory allocation overhead while preserving progressive filtering behavior.
