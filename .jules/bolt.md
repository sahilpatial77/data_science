## 2024-05-24 - Pandas Sequential Filtering vs Boolean Masking
**Learning:** Switching from sequential DataFrame filtering to a simple cumulative boolean mask for outlier removal can change the underlying mathematical behavior if quantiles aren't calculated progressively.
**Action:** To optimize performance (avoiding O(N) memory allocations) while preserving progressive filtering behavior, evaluate boolean masks cumulatively and compute quantiles on the progressively masked data (e.g., `df.loc[mask, col]`).
