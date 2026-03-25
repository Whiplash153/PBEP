# Task 2 — Decorators with Arguments

**Goal:**  
Learn how to create decorators that accept their own parameters, such as log levels or configuration options.

**What was done:**  
- Implemented a decorator `announce(level)` that takes an argument and customizes the output format.  
- Practiced the concept of nested functions:  
  1. `announce(level)` receives the parameter.  
  2. Returns an internal `decorator(func)`.  
  3. Which then returns `wrapper(*args, **kwargs)` that runs the original function.  
- Completed a mini-practice by creating a `tagged(tag)` decorator, which adds a prefix like `[INFO]` or `[DEBUG]` before each function’s output.

**Result:**  
Understood how Python processes `@decorator(args)` syntax and how it expands to multiple nested levels.  
Now any decorator can be made configurable and reusable for different contexts.