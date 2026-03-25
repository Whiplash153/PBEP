def safe_divide(a, b):
    if b == 0:
        raise ZeroDivisionError("zero divide")
    return a / b

def test(a, b):
    try:
        result = safe_divide(a, b)
    except ZeroDivisionError as e:
        print("Error:", e)
    else:
        print("Result:", result)
    finally:
        print("Done")

test(10, -2)
test(10, 0)



