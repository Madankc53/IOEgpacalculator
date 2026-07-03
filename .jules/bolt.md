## 2026-07-03 - Optimized calculation logic and resource loading
**Learning:** Caching DOM lookups and using `valueAsNumber` instead of `parseInt` significantly reduces JS execution time for form-heavy calculators. Adding `preconnect` hints for CDNs (Tailwind, Google Fonts) reduces initial load latency.
**Action:** Always check for repeated DOM lookups in event handlers and utilize `valueAsNumber` for numeric inputs to improve performance. Use `preconnect` for known external assets.
