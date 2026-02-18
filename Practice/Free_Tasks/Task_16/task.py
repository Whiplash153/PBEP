a = input("Type a:")
b = input("Type b:")

try:
    a = int(a)
    b = int(b)
    result = a / b
    print("Result:", result)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Can divide only numbers")
finally:
    print("Operation finished")