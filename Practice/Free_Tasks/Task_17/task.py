def safe_divide():
    try:
        a = int(input("Number 1: "))
        b = int(input("Number 2: "))
        result = a / b
        print("Result:", round(result))
        return result
    except ValueError:
        print("Wrong value")
        return None
    except ZeroDivisionError:
        print("Cannot divide by zero")
        return None
    finally:
        print("Done")

if __name__ == "__main__":
    safe_divide()