## 2026-07-02 - [Optimizing Numeric Input Access and DOM Lookups]
**Learning:** Using `HTMLInputElement.valueAsNumber` is more efficient than `parseInt(element.value)` for `type="number"` inputs as it retrieves the internal numeric value directly, avoiding redundant string parsing. Additionally, caching DOM references outside event listeners significantly reduces the execution time of repeated calculations.
**Action:** Always prefer `valueAsNumber` for numeric inputs and cache DOM lookups outside of hot paths (like click/submit handlers).
