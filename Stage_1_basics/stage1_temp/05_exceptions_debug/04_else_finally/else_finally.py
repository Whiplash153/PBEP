a = 10
b = 2

try:
    result = a / b
except ZeroDivisionError:
    print("Error: zero")
else:
    print("Result:", result)
finally:
    print("Program finished")