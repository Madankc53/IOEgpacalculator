## 2026-06-17 - [Optimizing DOM and Resource Loading]
**Learning:** Caching DOM element references outside of hot event listeners (like form submission) and using `valueAsNumber` instead of `parseInt` on numeric inputs significantly reduces per-calculation overhead and improves type safety. Adding `preconnect` resource hints for CDNs reduces the critical path latency for initial page loads.
**Action:** Always check for repeated DOM lookups in event handlers and utilize `valueAsNumber` for `type="number"` inputs to avoid unnecessary string parsing.
