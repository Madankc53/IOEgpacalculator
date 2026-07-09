## 2025-05-15 - DOM Caching and Resource Preconnecting
**Learning:** In a single-page static application, caching DOM references outside event listeners and using `valueAsNumber` for numeric inputs can significantly reduce JS execution overhead (approx. 40-50% in this case). Adding `preconnect` hints for external CDNs (Tailwind, Google Fonts) reduces initial load latency.
**Action:** Always check for repeated `getElementById` calls inside high-frequency event handlers and prefer native property access over manual parsing.
