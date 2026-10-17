## 2024-10-17 - Hardcoding Datetime Formats
**Learning:** Hardcoding a single datetime format string inside a loop over multiple dynamic date columns introduces brittleness if the columns contain different formats.
**Action:** Always verify that all target columns strictly adhere to the specified format before hardcoding it in a loop, or use column-specific formats.
