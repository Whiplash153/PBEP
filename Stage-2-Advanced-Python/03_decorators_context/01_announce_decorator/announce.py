def announce(func):
    def wrapper(*args, **kwargs):
        print(f"Beginning new function {func.__name__}...")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} complete.")
        return result
    return wrapper

@announce
def greet(name):
    print(f"Hello, {name}!")

greet("Mikhail")

