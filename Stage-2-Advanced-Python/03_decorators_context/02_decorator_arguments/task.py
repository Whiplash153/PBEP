def announce(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"[{level}] Starting {func.__name__}...")
            result = func(*args, **kwargs)
            print(f"[{level}] Finished {func.__name__}.")
            return result
        return wrapper
    return decorator

@announce("INFO")
def greet(name):
    print(f"Hello, {name}!")

greet("Mikahil")