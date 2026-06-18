## 2025-06-18 - [Optimization patterns in single-file apps]
**Learning:** In a single-file static HTML application, performance gains can be achieved by caching DOM element references outside event handlers to avoid repeated `document.getElementById` calls and by using `HTMLInputElement.valueAsNumber` for more efficient numeric retrieval.
**Action:** Always look for opportunities to move DOM lookups out of frequently called event listeners and prefer `valueAsNumber` over `parseInt` for numeric inputs.
