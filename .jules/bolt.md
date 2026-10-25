## 2023-10-24 - Pandas Sequential Masking Optimization
**Learning:** Reconstructing DataFrames inside loops via masking causes significant reallocation overhead. Using sequential boolean masks (like `mask &= ...`) and a single evaluation via `df.iloc[mask]` eliminates repeated memory allocations.
**Action:** Use sequential masking arrays or masks evaluated outside the loop when filtering iteratively across multiple columns.
