# Generator with Step Parameter

**Goal:**  
Learn how to create generators that accept parameters and control iteration behavior.

**Description:**  
This generator produces squares of numbers from `n` down to 1, decreasing by a specified `step` value each time.  
It demonstrates how a generator can manage both iteration logic and computation using parameters.

**Key points:**
- Uses `while` loop with conditional termination.
- Accepts two parameters: the start number and step size.
- Combines iteration with computation (`n ** 2`).
- Automatically raises `StopIteration` when the sequence ends.