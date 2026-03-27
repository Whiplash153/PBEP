def safe_divide(a):
    if a < 0:
        raise ValueError("negative not allowed")
    return a

print(safe_divide(-2))
