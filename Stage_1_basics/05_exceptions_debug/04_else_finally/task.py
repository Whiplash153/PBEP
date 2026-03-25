a = 455
b = 0

try:
    result = a / b
except ZeroDivisionError:
    print("Error: zero")
else:
    print("Result:", result)
finally:
    print("Done")