# Task 6: practice safe_divide

**What I did**  
Created a safe division function that uses `raise`, `try/except`, `else`, and `finally`.

**What I learned**  
- How to combine error handling tools in one program.  
- `raise` can generate errors with custom messages.  
- `try/except` catches errors and prevents crashes.  
- `else` runs only if no error happened.  
- `finally` always runs at the end.

**Practice**  
In `task.py`, I tested:  
- Division with a negative denominator → got `-5.0`.  
- Division by zero → caught the error `"zero divide"`.  
In both cases, `"Done"` was printed in the `finally` block.