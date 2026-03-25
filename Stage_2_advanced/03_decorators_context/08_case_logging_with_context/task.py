from logger_context import open_log
from logger_decorator import logger

@logger
def greet(name):
    print(f"Hello, {name}!")

@logger
def add(a, b):
    print(f"Result: {a + b}")
    return a + b

if __name__ == "__main__":
    with open_log("log.txt") as log:
        log.write("=== Program started ===\n")
        greet("Michael")
        add(3, 7)
        log.write("=== Program finished ===\n")
