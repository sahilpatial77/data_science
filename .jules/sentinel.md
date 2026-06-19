## 2026-06-19 - Missing gitignore exposes datasets
**Vulnerability:** The repository lacked a .gitignore file, which could easily lead to sensitive data (like "crime dataset.csv") being committed to the repo.
**Learning:** In a data science repository, datasets are usually placed in the root directory. Without a .gitignore, raw data might be checked in alongside code, exposing PII or other sensitive information.
**Prevention:** Always ensure a repository has a .gitignore file configured with patterns for standard build artifacts, environment files, and datasets (*.csv, etc).
