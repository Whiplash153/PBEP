# Task 5: raise

**What I did**  
Created a function that checks input and raises an error if the value is invalid.

**What I learned**  
- `raise` is used to generate errors manually.  
- You can provide a custom message for clarity.  
- Example: `raise ValueError("negative not allowed")`.

**Practice**  
In `task.py`, I wrote `safe_divide(a)`:
- If `a < 0` → the function raises `ValueError`.  
- If `a >= 0` → the function returns the number.  