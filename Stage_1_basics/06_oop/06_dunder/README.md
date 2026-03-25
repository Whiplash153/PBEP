# Task 6: Dunder methods

**What I did**  
- Created a `Person` class with a `__str__` method to make objects printable in a readable way.  
- Added a `Student` subclass with its own `__str__` that also shows the major.  
- In `demo.py`, demonstrated how `Person` and `Student` objects are printed nicely in a list.  
- In `task.py`, implemented a `Book` class with `__str__`, so a list of books prints in a clear format.

**What I learned**  
- Dunder (special) methods start and end with `__` (e.g., `__init__`, `__str__`).  
- `__str__` defines how an object is displayed when printed.  
- Without `__str__`, Python shows only a technical reference like `<__main__.Class object at 0x...>`.  
- With `__str__`, objects can return human-friendly strings, which is useful for both users and debugging.