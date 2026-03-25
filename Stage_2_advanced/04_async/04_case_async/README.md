# Case: Asynchronous Data Loading

**Goal:**  
Combine all previous async concepts to perform parallel data loading from multiple sources.

**What was done:**  
- Created asynchronous function `load_data()` to fetch text data from several URLs.  
- Used `aiohttp.ClientSession()` for safe session management and `asyncio.gather()` for concurrent execution.  
- Measured total execution time and confirmed all requests ran in parallel.  
- Demonstrated full workflow: async function creation → concurrent network calls → data aggregation.

**Key point:**  
This case shows how asynchronous programming efficiently handles multiple I/O operations  
without blocking the event loop, reducing total execution time to that of the slowest task.