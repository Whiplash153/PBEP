# Case: Vector Class

### Task  
Create a `Vector` class that demonstrates the use of extended dunder (magic) methods.  

### What was done  
This task implements a class that simulates the behavior of a mathematical vector.  
It combines several key dunder methods to make the object behave like a native Python type:  

1. **Initialization:**  
   `__init__` sets up the vector coordinates when an object is created.  

2. **Arithmetic operations:**  
   `__add__` allows adding two vectors and returns a new `Vector` object.  

3. **Comparison:**  
   `__eq__` compares the coordinates of two vectors and returns the comparison result.  

4. **Iteration:**  
   `__iter__` makes the vector iterable, allowing it to be used in a `for` loop.  

5. **Length:**  
   `__len__` returns the number of coordinates (the vector’s dimension).  

6. **Representation:**  
   `__repr__` provides a clear, developer-friendly representation of the object in the console.  

### Result  
With these dunder methods, the `Vector` object behaves like a built-in Python type —  
it can be added, compared, iterated over, and printed in a human-readable form.