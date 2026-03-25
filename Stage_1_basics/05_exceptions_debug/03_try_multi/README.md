# Task 3: multiple except

**What I did**  
Wrote code with two possible errors inside one `try` block: division by zero and undefined variable.

**What I learned**  
- `try` can have multiple `except` blocks.  
- Only the matching `except` runs, depending on the error type.  
- Example:  
  - `ZeroDivisionError` → when dividing by zero.  
  - `NameError` → when using a variable that does not exist.

**Practice**  
In `task.py`, I tested both cases:  
- With `b = 0` → printed `"Error: zero"`.  
- With `b = 1` → printed `"Result: 500.0"` and then `"Error: name"`.