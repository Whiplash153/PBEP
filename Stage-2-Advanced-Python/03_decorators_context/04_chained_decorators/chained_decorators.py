from functools import wraps

def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOGGER] Start {func.__name__}")
        result = func(*args, **kwargs)
        print(f"[LOGGER] End {func.__name__}\n")
        return result
    return wrapper

def authenticate(func):
    @wraps(func)
    def wrapper(is_authorized, *args, **kwargs):
        print(f"[AUTH] Checking access for {func.__name__}...")
        if not is_authorized:
            print(f"[AUTH] Access denied to {func.__name__}.")
            return
        print(f"[AUTH] Access granted to {func.__name__}!")
        return func(*args, **kwargs)
    return wrapper

@logger
@authenticate
def greet(name):
    print(f"Hello, {name}!")

@authenticate
@logger
def bye(name):
    print(f"Bye, {name}!")

if __name__ == "__main__":
    greet(True, "Alice")
    bye(False, "Alice")
