## 2026-07-01 - Optimizing Static HTML Calculator
**Learning:** For single-file static applications, major performance wins come from reducing network latency (preconnect hints) and micro-optimizing DOM access (caching elements outside event loops). `valueAsNumber` is a faster alternative to `parseInt` for numeric inputs.
**Action:** Always check for external CDNs and add `preconnect` hints. Cache DOM lookups if they occur inside high-frequency events or even standard form submissions.
