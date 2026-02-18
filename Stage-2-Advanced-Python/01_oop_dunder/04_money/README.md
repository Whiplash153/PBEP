# Money with Arithmetic Operations

We created a `Money` class that supports arithmetic operations and comparison.

## Implemented dunder methods
- `__add__` → adds two amounts (only if currencies match)
- `__sub__` → subtracts two amounts (only if currencies match)
- `__eq__` → compares amounts and currencies
- `__str__` → formats the amount like `100.00 USD`
- `__repr__` → developer-friendly debug output

## Example
```python
from money import Money

usd1 = Money(50, "USD")
usd2 = Money(25.75, "USD")
eur1 = Money(10, "EUR")

print(usd1)   # 50.00 USD
print(usd2)   # 25.75 USD

print(usd1 + usd2)  # 75.75 USD
print(usd1 - usd2)  # 24.25 USD
print(usd1 == usd2)  # False
print(usd1 == Money(50, "USD"))  # True

try:
    total = usd1 + eur1
    print(total)
except ValueError as e:
    print("Error:", e)

# Output:
# 50.00 USD
# 25.75 USD
# 75.75 USD
# 24.25 USD
# False
# True
# Error: Different currencies