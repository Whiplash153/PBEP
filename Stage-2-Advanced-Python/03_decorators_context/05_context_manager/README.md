# Task 5 — Context Managers: Basic Principle

**Goal:**  
Understand how Python manages resources with the `with` statement and learn to create custom context managers using `__enter__` and `__exit__`.

**What was done:**  
- In `file_manager.py` — demonstrated the difference between manual file handling and using `with open()`.  
- In `custom_manager.py` — implemented a custom class `FileManager` with `__enter__` and `__exit__` methods that automatically open and close files.  
- In `safe_manager.py` — extended the class to `SafeFileManager`, which handles errors inside `__exit__` and prevents program crashes (`return True` suppresses exceptions).  
- In `task.py` — created a small practical example that writes and reads a file using `SafeFileManager`, verifying that even if an error occurs, the file closes correctly and the program continues.

**Result:**  
- Learned how context managers simplify resource management.  
- Confirmed that `__exit__` executes even when exceptions occur.  
- The program finished with `exit code 0`, showing that the exception was properly handled and suppressed.