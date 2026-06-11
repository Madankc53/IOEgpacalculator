## 2026-06-11 - [DOM Caching and Input Optimization]
**Learning:** Caching DOM elements outside of frequently triggered event listeners (like 'submit') and using native properties like `valueAsNumber` provides a cleaner and more efficient way to handle numeric inputs in vanilla JS applications compared to repeated lookups and manual string parsing.
**Action:** Always check for repeated `document.getElementById` calls within event loops or handlers and refactor them to use a cached lookup object.

## 2026-06-11 - [Resource Pre-hints]
**Learning:** For static single-page apps using external CDNs for CSS (Tailwind) and fonts (Google Fonts), adding `preconnect` hints for both the API domain (`fonts.googleapis.com`) and the asset domain (`fonts.gstatic.com` with `crossorigin`) is essential for minimizing the critical request chain latency.
**Action:** Implement `preconnect` for all external CDNs used for critical styling or font assets.
