# Case: NumberCatalog

**Goal:**  
Combine iterators and generators in one program to simulate real data streaming and filtering.

**Description:**  
The `NumberCatalog` class behaves like a small data stream.  
It can be iterated over to produce numbers from `start` to `end`, and it also contains a generator method `even_squares()` that yields only even squares within that range.  
This demonstrates how iterator protocols (`__iter__`, `__next__`) and `yield` can coexist in one class to handle both sequential access and filtered generation.

**Key points:**
- Implements the iterator protocol (`__iter__`, `__next__`).
- Provides a generator method using `yield`.
- Filters values dynamically (even squares only).
- Simulates real-world stream processing logic without storing all data in memory.