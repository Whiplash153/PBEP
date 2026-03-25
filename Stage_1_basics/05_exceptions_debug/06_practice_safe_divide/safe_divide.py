def safe_divide(a, b):
    if b == 0:
        raise ZeroDivisionError("cannot divide by zero")
    return a / b

def demo(a, b):
    try:
        result = safe_divide(a, b)
    except ZeroDivisionError as e:
        print("Error:", e)
    else:
        print("Result:", result)
    finally:
        print("Done")

demo(10, 2)
demo(10, 0)