# Asynchronous HTTP requests with aiohttp

**Goal:**  
Learn how to send multiple HTTP requests asynchronously using `aiohttp` and handle responses concurrently.

**What was done:**  
- Created asynchronous function `fetch_data()` to send requests and read responses with `await response.text()`.  
- Used `aiohttp.ClientSession()` to manage all requests safely within a single session.  
- Launched all requests simultaneously with `asyncio.gather()`.  
- Measured and displayed total execution time to confirm concurrent behavior.

**Key point:**  
`aiohttp` integrates seamlessly with `asyncio`, allowing multiple I/O-bound operations (like network calls)  
to run concurrently without blocking the event loop.