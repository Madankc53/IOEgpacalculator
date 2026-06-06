## 2025-05-15 - Optimize Calculation Path and Resource Loading

**Learning:** In small, interactive Vanilla JS applications, DOM lookups and string parsing in tight loops or event handlers are common bottlenecks. Pre-caching DOM elements and using `HTMLInputElement.valueAsNumber` provides a cleaner, more performant way to handle numeric inputs. Additionally, resource hints like `preconnect` for critical third-party assets (like Google Fonts) can noticeably reduce the time to first meaningful paint.

**Action:** Always cache frequently accessed DOM elements outside event listeners and prefer `valueAsNumber` for numeric input fields. Implement `preconnect` or `dns-prefetch` for essential CDN-hosted resources.
