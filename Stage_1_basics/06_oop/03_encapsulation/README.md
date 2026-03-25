# Task 3: Encapsulation

**What I did**  
Implemented a class `Account` with a protected attribute `_balance` and methods to safely manage money.  

**What I learned**  
- Encapsulation hides internal state of the object.  
- Attributes with `_` are considered protected: they should not be changed directly.  
- Methods (`deposit`, `withdraw`, `get_balance`) control safe access and modification of data.  

**Practice**  
- In `demo.py`, tested deposits and withdrawals with different accounts.  
- In `task.py`, created an account with zero balance, attempted invalid withdrawal, then deposit and valid withdrawal, and printed final balance.