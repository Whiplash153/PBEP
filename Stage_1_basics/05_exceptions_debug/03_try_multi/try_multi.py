a = 10
b = 2

try:
    result = a / b
    print("Result:", result)
    print(user_name)
except ZeroDivisionError:
    print("Error: zero div")
except NameError:
    print("Error: name")
