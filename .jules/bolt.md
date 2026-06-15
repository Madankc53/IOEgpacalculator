## 2026-06-15 - DOM Caching and Efficient Value Retrieval
**Learning:** In static single-page applications, repeatedly querying the DOM with `document.getElementById` inside event handlers is a common but avoidable bottleneck. Additionally, using `parseInt(element.value)` is slower and more error-prone than `element.valueAsNumber` for `type="number"` inputs.
**Action:** Always cache DOM element references outside of hot paths (like form submit or input event handlers) and prefer `valueAsNumber` for numeric inputs to avoid redundant string parsing.

## 2026-06-15 - Early Connection with Resource Hints
**Learning:** External assets like Google Fonts and CDNs can introduce significant latency due to DNS lookup, TCP handshake, and TLS negotiation.
**Action:** Use `<link rel="preconnect">` for critical third-party domains to start these connections as early as possible, reducing the overall page load time.
