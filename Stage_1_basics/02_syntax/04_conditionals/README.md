# Conditional Constructions (if/elif/else)

**Stage/Topic/Task:** Stage 1 → Syntax → Conditional constructions

**Goal:** Learn how to control program flow with conditional statements.

**What I did:**
- Practiced basic `if`, `if/else`, and `if/elif/else`.
- Combined conditions with logical operators `and`, `or`, `not`.
- Compared nested conditions vs flat `elif` chains.
- Worked with user input (`input()` + `int()`) for interactive checks.
- Built a mini-case: access system with login and age:
  - `admin` → always access.
  - `vip` → access from age 16.
  - other users → access from age 18.
  - otherwise → denied.

**What I learned:**
- Conditional blocks execute only if the condition is `True`.
- `if x:` means "if x == True".
- Conditions are checked top-to-bottom; only the first match runs.
- You can avoid unnecessary checks by placing the most specific rules first.
- Input from the user is always a string; convert to `int` if needed.

**How to run:**
```bash
python 02_syntax/04_conditionals/basic.py
python 02_syntax/04_conditionals/logic.py
python 02_syntax/04_conditionals/input.py