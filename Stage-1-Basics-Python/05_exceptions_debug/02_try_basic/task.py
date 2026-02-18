a = 999
b = 0

try:
    result = a / b
    print("result:", result)
except ZeroDivisionError:
    print("Error: divide by zero")