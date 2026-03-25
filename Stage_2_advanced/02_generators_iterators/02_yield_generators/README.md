# Yield and Simple Generators

**Goal:**  
Learn how to use the `yield` keyword to create simple generators in Python.

**Description:**  
This task demonstrates how a generator can produce values one by one without storing them in memory.  
The example function uses `yield` inside a `for` loop to return the squares of numbers from `n` down to 1.  
It shows how generators remember their state between iterations and automatically raise `StopIteration` when finished.

**Key points:**
- `yield` turns a function into a generator.
- Values are produced lazily (on demand).
- The loop `for` handles iteration automatically.