## 2026-06-05 - [Initial Assessment]
**Learning:** The application is a single-file HTML with Tailwind CSS loaded via CDN, which is a major performance bottleneck for initial load and rendering. However, without a build system, replacing it is out of scope for a 'small' improvement. DOM lookups are performed repeatedly on every form submission.
**Action:** Cache DOM elements and simplify calculations to improve responsiveness.
## 2026-06-05 - [DOM Caching and Math Optimization]
**Learning:** In simple Vanilla JS applications, repeated DOM lookups and high-level array methods like `Object.values().reduce()` are common but avoidable performance drains in hot paths like form submission. Factoring out multipliers in repetitive calculations also reduces floating-point operations.
**Action:** Always cache DOM elements used in event listeners and prefer direct property access/summation over generic iterators for small, fixed-size data structures.
