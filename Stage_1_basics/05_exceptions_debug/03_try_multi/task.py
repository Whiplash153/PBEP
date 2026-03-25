a = 500
b = 1

try:
    result = a / b
    print("a / b:", result)
    print(user_name)
except ZeroDivisionError:
    print("Error: zero")
except NameError:
    print("Error: name")
