## 2025-05-15 - Optimizing DOM access and numeric retrieval in Vanilla JS

**Learning:** Caching DOM element references outside of high-frequency event listeners (like 'submit') and using `HTMLInputElement.valueAsNumber` instead of `parseInt(input.value)` significantly reduces JS execution time in calculation-heavy forms. Additionally, direct arithmetic summation is faster than `Object.values().reduce()` due to avoiding intermediate array creation.

**Action:** Always look for opportunities to hoist DOM lookups and use native numeric properties for inputs in performance-critical paths.
