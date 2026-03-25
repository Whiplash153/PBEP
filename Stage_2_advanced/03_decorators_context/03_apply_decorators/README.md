# Task 3 — Applying Decorators

**Goal:**  
Practice using decorators in real examples to see how they can control and extend function behavior.

**What was done:**  
- Implemented three decorators in `advanced_decorators.py`:  
  `logger`, `cache`, and `validate_positive`.  
- In this mini-practice, imported `logger` and applied it to three functions:
  - `greet(name)` — prints a greeting,  
  - `add(a, b)` — prints the sum,  
  - `say_goodbye(name)` — prints a goodbye message.  
- Verified that each function logs its start and finish correctly.

**Result:**  
Learned how decorators can add behavior without changing the original function’s code.  
The `logger` decorator now works as a simple monitoring tool for any function.