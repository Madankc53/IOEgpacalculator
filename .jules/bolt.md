## 2026-06-19 - DOM Caching and Efficient Numeric Retrieval
**Learning:** In interactive static applications like calculators, repetitive DOM lookups within event listeners and redundant string parsing (e.g., `parseInt(el.value)`) can introduce unnecessary overhead. Caching DOM element references outside the event loop and utilizing `HTMLInputElement.valueAsNumber` for numeric inputs significantly optimizes execution speed and memory efficiency.
**Action:** Always cache frequently accessed DOM elements at the top level and prefer `valueAsNumber` over manual parsing for `type="number"` inputs.
