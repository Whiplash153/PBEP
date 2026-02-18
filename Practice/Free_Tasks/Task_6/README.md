# Task: Calculate Total Expenses

## Condition
A user provides a list of daily expenses that may contain invalid values such as letters or empty strings.  
The goal is to calculate the total sum of valid expenses and safely skip incorrect values.

## Solution
We used a **for-loop** to iterate through each element in the list.  
Inside the loop, each value is converted to an integer inside a **try/except** block.  
If conversion fails (raises `ValueError`), the value is skipped using `continue`.  
Finally, the program prints the total sum.

**Tools used:** list, for-loop, int(), try/except, continue, print.