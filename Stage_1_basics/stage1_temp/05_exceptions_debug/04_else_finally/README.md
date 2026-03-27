# Task 4: else and finally

**What I did**  
Used `try/except/else/finally` to handle division and always finish cleanly.

**What I learned**  
- `else` runs only if no error happened in `try`.  
- `finally` runs always (with or without errors).  
- Example error: `ZeroDivisionError` when dividing by zero.

**Practice**  
In `task.py`, I tried `a / b`:
- If `b == 0` → print an error message.
- Otherwise → print the result.
In both cases, print `"Done"` in `finally`.