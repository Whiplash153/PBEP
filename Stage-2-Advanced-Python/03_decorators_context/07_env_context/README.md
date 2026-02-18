# Task 7 — Contextlib and @contextmanager

**Goal:**  
Learn how to create a context manager using the `@contextmanager` decorator from the `contextlib` module and understand how it automatically handles entering and exiting a block.

---

### 🧩 What was done:
- Implemented a context manager `safe_change_dir()` using `@contextmanager`.
- The manager temporarily changes the current working directory, handles possible errors, and always restores the previous directory.
- Tested how `yield` splits the execution flow into **enter** and **exit** phases.
- Confirmed that code after `yield` executes even when an exception occurs inside the `with` block.

---

### 🧪 Files:
- **`env_context.py`** — base example of a simple context manager with `yield`.
- **`safe_env_context.py`** — improved version with `try / except / finally` for error handling.
- **`task.py`** — mini-practice that verifies how the manager behaves when switching directories and encountering an error.

---

### 📘 Result:
- Entered `/tmp`, executed code, simulated an error, caught it, and returned to the original directory.  
- `yield` successfully acted as a pause between *entering* and *exiting* the context.  
- The program finished with `exit code 0`, confirming proper error handling.