def square(x, y):
    if x <= 0:
        return "Invalid size"
    elif y <= 0:
        return "Invalid size"
    return x * y

result = square(30, 40)
print(result)

result = square(30, 0)
print(result)

result = square(-2, 40)
print(result)