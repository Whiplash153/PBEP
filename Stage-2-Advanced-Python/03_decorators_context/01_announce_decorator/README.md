# Task 1 — Principle of Decorator Work

**Goal:**  
Understand how a decorator wraps a function and adds behavior before and after its execution.

**What was done:**  
- Created a base decorator `announce`, which prints messages before and after a function call.  
- Tested it on a sample function to demonstrate how Python replaces the original function with the wrapper.  
- Implemented a mini-practice — a decorator `notice`, which works with any function and adds notification-style messages.

**Result:**  
Learned how to use `@decorator` syntax and understood that it’s equivalent to `function = decorator(function)`.  
The concept of wrapping functions and controlling their execution flow is now clear.