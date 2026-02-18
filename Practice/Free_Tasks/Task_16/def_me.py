def safe_divide():
    try:
        a = int(input("Type a:"))
        b = int(input("Type b:"))
        result = round(a / b)
        print("Result:", result)
    except ZeroDivisionError:
        print("Cannot divide by zero")
    except ValueError:
        print("Can divide only numbers")
    finally:
        print("Operation finished")

safe_divide()