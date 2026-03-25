from advanced_decorators import logger

@logger
def greet(name):
    print(f"Hello, {name}!")

@logger
def add(a, b):
    print("Sum:", a + b)

@logger
def say_goodbye(name):
    print(f"See you, {name}!")

greet("Michael")
add(5, 10)
say_goodbye("Michael")