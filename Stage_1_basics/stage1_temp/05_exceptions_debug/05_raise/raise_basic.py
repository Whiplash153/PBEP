def safe_divide(a, b):
    if b == 0:
        raise ZeroDivisionError ("b must not be zero")
    return a / b

print(safe_divide(10, 2))
print(safe_divide(10, 0))