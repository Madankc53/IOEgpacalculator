## 2026-07-08 - Optimized DOM Access and Resource Loading
**Learning:** Caching DOM element references outside of high-frequency event listeners (like form submission) and using direct property access instead of object iteration (e.g., Object.values().reduce()) provides a measurable reduction in JS execution time, even for small applications.
**Action:** Always look for repeated 'document.getElementById' calls in event handlers and move them to a cache. Use valueAsNumber for numeric inputs to avoid string parsing overhead.
