def logger(func):
    def wrapper(*args, **kwargs):
        with open("log.txt", "a", encoding="utf-8") as log:
            log.write(f"[LOG] Started: {func.__name__}\n")
            result = func(*args, **kwargs)
            log.write(f"[LOG] Finished: {func.__name__}\n")
        return result
    return wrapper

@logger
def greet(name):
    print(f"Hello, {name}!")

if __name__ == "__main__":
    greet("Michael")