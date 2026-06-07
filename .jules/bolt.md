## 2024-05-24 - Optimize existence checks
**Learning:** Using `.sum() > 0` forces full-column traversal. The `.hasnans` property short-circuits and avoids unnecessary iteration.
**Action:** Always prefer `.hasnans` or `.any()` when checking for missing values.
