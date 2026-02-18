# asyncio.gather and sleep

**Goal:**  
Understand how to execute multiple asynchronous coroutines concurrently using `asyncio.gather()`.

**What was done:**  
- Created three coroutines (`coro1`, `coro2`, `coro3`) with different delays using `await asyncio.sleep()`.  
- Executed them concurrently with `await asyncio.gather(...)`.  
- Measured total execution time and confirmed that concurrent tasks finish in the time of the longest coroutine.

**Key point:**  
`asyncio.gather()` allows several coroutines to run at the same time inside one event loop,  
so tasks overlap instead of waiting for each other to finish.