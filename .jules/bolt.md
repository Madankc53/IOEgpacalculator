## 2025-05-15 - Frontend Efficiency Optimization
**Learning:** Preconnect resource hints for external CDNs (Tailwind, Google Fonts) significantly reduced load time in this environment (from ~1442ms to ~400ms). Caching DOM elements outside frequent event handlers and using `valueAsNumber` for numeric inputs provided a cleaner and slightly more efficient implementation.
**Action:** Always prioritize preconnect/preload for critical external assets and cache DOM lookups when performing repeated calculations on the same elements.
