## 2024-06-13 - [Missing Dataset Gitignore]
**Vulnerability:** The repository lacks a .gitignore file, risking accidental commit of sensitive data files.
**Learning:** Data science projects often process sensitive offline datasets that must be explicitly excluded from version control to prevent data leaks.
**Prevention:** Always initialize data science repositories with a .gitignore tailored to exclude data files (*.csv) and secrets (.env).
