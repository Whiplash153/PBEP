a = 10
b = 0

try:
    result = a / b
    print("Result:", result)
except ZeroDivisionError:
    print("Error: divide by zero")