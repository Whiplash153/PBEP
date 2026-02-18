# Task 8 — Case: Logging to File with Decorator + Context Manager

**Goal:**  
Combine a decorator and a context manager into a single working program.  
Learn how to separate responsibilities:  
- the context manager manages the file resource,  
- the decorator manages the function’s behavior.

---

### 🧩 What was done:
- **`logger_context.py`** — created a context manager `open_log()` that opens a file,  
  writes the start and end of a logging session, and guarantees file closure.  
- **`logger_decorator.py`** — implemented a decorator `@logger` that logs the start and end  
  of each decorated function’s execution.  
- **`task.py`** — combined both mechanisms:
  - the program starts and ends a logging session through `with open_log(...)`,
  - decorated functions (`@logger`) automatically record their calls inside the same log.