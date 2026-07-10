## 2025-05-15 - DOM Lookup and Numeric Retrieval Optimization
**Learning:** In static HTML applications with frequent calculations triggered by events, repeated `document.getElementById` and `parseInt(element.value)` calls create measurable overhead. Caching elements in an object and using `HTMLInputElement.valueAsNumber` significantly improves execution speed by avoiding redundant DOM traversals and string parsing.
**Action:** Always cache DOM references outside high-frequency event handlers and prefer `valueAsNumber` for numeric inputs.

## 2025-05-15 - Initial Load Performance with Preconnect
**Learning:** External CDNs for CSS (Tailwind) and Fonts (Google Fonts) can introduce significant connection latency. Adding `preconnect` resource hints in the `<head>` reduces this latency by initiating early handshakes.
**Action:** Use `preconnect` for all critical external CDN resources to improve the Largest Contentful Paint (LCP) and overall load experience.
