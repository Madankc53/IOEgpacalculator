## 2025-05-15 - DOM Lookup and Resource Optimization
**Learning:** In a single-file static application, repeated DOM lookups and network handshakes for CDNs are low-hanging fruit. Caching elements outside event handlers and using preconnect hints significantly reduce perceived and actual latency.
**Action:** Always check for early connection opportunities for external assets and ensure DOM lookups in high-frequency event listeners (like form submissions) are cached.

**Learning:** Truncation of tool outputs can lead to invalid plans if variable names or logic are assumed.
**Action:** Use incremental reads (sed/read_file with offsets) to ensure the entire scope of a script is visible before proposing refactors.
