# Async / Await Basics

**Goal:**  
Understand how `async` and `await` work in Python and how to pause execution using `await`.

**What was done:**  
- Created an asynchronous function `boil_water()` that simulates a delayed operation with `await asyncio.sleep()`.  
- Added an extra awaited step to imitate making tea after boiling water.  
- Used `asyncio.run()` to start the event loop and execute the coroutine.

**Key point:**  
`await` allows the program to pause inside an async function until the awaited operation is completed, without blocking the entire program.