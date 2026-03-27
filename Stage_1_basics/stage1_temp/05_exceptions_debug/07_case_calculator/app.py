def safe_calculator(expr):
    try:
        a_str, op, b_str = expr.split()

        a = float(a_str)
        b = float(b_str)

        if op == "/":
            if b == 0:
                raise ZeroDivisionError("division by zero")
            return a / b
        elif op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        else:
            raise ValueError("unsupported operator")

    except ValueError as e:
        return f"Input error: {e}"
    except ZeroDivisionError as e:
        return f"Math error: {e}"
    except Exception as e:
        return f"Unexpected error: {e}"
    finally:
        print("Calculation finished")

print(safe_calculator("12 / 3"))
print(safe_calculator("10 / 0"))
print(safe_calculator("5 & 2"))
print(safe_calculator("abc / 2"))