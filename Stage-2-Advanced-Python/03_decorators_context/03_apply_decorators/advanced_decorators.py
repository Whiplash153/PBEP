def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Function {func.__name__} started")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} complete\n")
        return result
    return wrapper

def cache(func):
    storage = {}

    def wrapper(*args):
        if args in storage:
            print(f"Using cache result for {args}")
            return storage[args]
        print(f"Calculating and saving result for {args}\n")
        result = func(*args)
        storage[args] = result
        return result
    return wrapper

def validate_positive(func):
    def wrapper(*args):
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:
                print(f"Error: {arg} is negative")
                return
        return func(*args)
    return wrapper

@logger
def greet(name):
    print(f"Hello, {name}!")

@cache
def multiply(a, b):
    return a * b

@validate_positive
def square(n):
    print(f"Square of {n} = {n ** 2}")

if __name__ == "__main__":
    greet("Michael")
    print(multiply(3, 4))
    print(multiply(3, 4))
    square(5)
    square(-2)
