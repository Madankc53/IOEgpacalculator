## 2026-06-14 - DOM caching and valueAsNumber optimization
**Learning:** Caching DOM elements outside of event listeners and using `valueAsNumber` instead of `parseInt(value)` for number inputs significantly reduces the overhead on the main thread during repetitive user interactions like form submissions.
**Action:** Always check for repeated `getElementById` calls in event handlers and prefer native numeric properties for number inputs.
