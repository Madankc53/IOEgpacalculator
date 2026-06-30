## 2026-06-30 - Resource Hints and DOM Optimization
**Learning:** Adding `preconnect` resource hints for CDNs (Tailwind, Google Fonts) significantly reduces initial load time by initiating early connections. In Vanilla JS, caching DOM elements outside frequent event listeners and using `valueAsNumber` instead of `parseInt` provides measurable speedups for interactive calculators.
**Action:** Always check for external assets that can be preconnected and cache DOM references when they are reused in high-frequency event handlers.
