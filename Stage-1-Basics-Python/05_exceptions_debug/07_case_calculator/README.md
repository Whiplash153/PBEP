# Case: Safe Calculator

**What I did**  
Built a mini calculator that reads a string expression like `"12 / 3"`, parses it, performs the calculation, and handles errors.

**What I learned**  
- How to parse a string into parts using `split()`.  
- How to convert strings into numbers with `float()`.  
- How to handle invalid input with `try/except`.  
- How to raise custom errors for division by zero and unsupported operators.  
- How to use `finally` to always show a completion message.

**Practice**  
Tested the program with different inputs:  
- `"12 / 3"` → `4.0`  
- `"10 / 0"` → `Math error: division by zero`  
- `"5 & 2"` → `Input error: unsupported operator`  
- `"abc / 2"` → `Input error: could not convert string to float`