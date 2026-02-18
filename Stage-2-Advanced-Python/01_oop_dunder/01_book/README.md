# Book class with dunder methods

In this task we created a `Book` class and practiced several dunder methods:

- `__init__` – initializes book objects with title and author.  
- `__str__` – defines how the object is printed with `print()`.  
- `__repr__` – defines how the object looks in console/debugging.  
- `__eq__` – compares books for equality (title and author).  
- `__lt__`, `__gt__` – allow comparing books by title alphabetically.  

### Example

```python
b1 = Book("1984", "Orwell")
b2 = Book("War", "Tolstoy")
b3 = Book("1984", "Orwell")

print(b1 == b2)   # False
print(b1 == b3)   # True
print(b1 < b2)    # True
print(b1 > b2)    # False
print(b1)         # Book: 1984 by Orwell
print(repr(b1))   # Book(title='1984', author='Orwell')
```