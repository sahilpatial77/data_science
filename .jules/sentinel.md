## 2024-05-24 - Missing gitignore file
**Vulnerability:** Accidental commit of sensitive data (PII, secrets)
**Learning:** The project lacked a `.gitignore` file, making it easy to accidentally commit datasets or secrets to the repository.
**Prevention:** Added a `.gitignore` file to ignore datasets, secrets, and Python artifacts.
