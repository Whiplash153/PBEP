# Filtered Squares Generator

**Goal:**  
Practice combining `yield` with conditions and parameters in generators.

**Description:**  
This generator produces only even squares of numbers, starting from `n` and decreasing by a given `step`.  
The sequence stops automatically when the square becomes less than 1000.  
It demonstrates how to use `yield` together with conditions and breaking logic to control generator flow.

**Key points:**
- Uses `while` loop with `if` filtering.
- Applies arithmetic operations (`**`, `-= step`).
- Includes a conditional stop (`if square < 1000: break`).
- Generates values one by one instead of building a full list.