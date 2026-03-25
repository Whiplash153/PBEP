# Task 4 — Chained Decorators

**Goal:**  
Understand how multiple decorators interact and affect the order of function execution.

**What was done:**  
- Implemented two decorators:
  - `logger` — logs when a function starts and finishes.
  - `authenticate` — checks access and blocks execution if not authorized.
- Applied them in different orders:
  - `@logger @authenticate` (logger outside)
  - `@authenticate @logger` (authenticate outside)
- Added a flag `is_authorized` to control access directly from function calls.

**Result:**  
- When `@logger` is outside, the logger runs even if access is denied.  
- When `@authenticate` is outside, logging happens only for authorized users.  
- Demonstrated how decorator order can change behavior and output logic.