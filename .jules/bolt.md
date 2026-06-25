## 2026-06-25 - Frontend Optimization: Preconnect & DOM Caching
**Learning:** Adding preconnect resource hints for CDN-delivered assets (Tailwind, Google Fonts) significantly reduced load time in this environment (from ~1443ms to ~499ms). Caching DOM lookups and using .valueAsNumber slightly improved calculation responsiveness, though the bottleneck in high-frequency execution remains the browser's event handling and DOM updates.
**Action:** Always prioritize preconnect for critical third-party CSS/JS in static HTML apps. Use .valueAsNumber for numeric inputs to avoid redundant parsing.
