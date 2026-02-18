# Task 6 — Custom Context Manager (ChangeDir)

**Goal:**  
Learn how to create a custom context manager through a class with `__enter__` and `__exit__` methods,  
and how it can manage system resources — in this case, switching and restoring working directories.

---

### 🧩 What was done:
- **`change_dir.py`** — implemented a simple class `ChangeDir`, which:
  - saves the current working directory,
  - switches to a new one when entering the `with` block,
  - and automatically restores the previous directory after exiting.
- **`safe_change_dir.py`** — added `SafeChangeDir`, which:
  - catches errors inside the `with` block,
  - logs them, and
  - prevents the program from crashing by returning `True` from `__exit__`.
- **`task.py`** — practical test:
  - verified that directory switching and restoration work correctly;
  - confirmed that even with an error (`1 / 0`), the directory returns to its original state;
  - created a folder `test_dir` and successfully wrote a file inside it.

---

### 📘 Result:
- Learned to manage directories safely using custom context managers.
- Verified that `__exit__` executes even when an exception occurs.
- Understood the use of `return True` for suppressing exceptions.
- Program completed successfully (`exit code 0`).