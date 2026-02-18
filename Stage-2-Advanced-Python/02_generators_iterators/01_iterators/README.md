# Countdown Iterator

**Goal:**  
Learn how to create a simple iterator in Python using the `__iter__` and `__next__` methods.

**Description:**  
The `Countdown` class demonstrates how iteration works under the hood in Python.  
It starts from a given number and returns each value down to 1, raising `StopIteration` when finished.  
The example shows how objects can manage their own iteration logic without using built-in loops.

**Key points:**
- Implements the iterator protocol.
- Uses `__iter__` to return the iterator object itself.
- Uses `__next__` to return the next value and handle the end of the sequence.