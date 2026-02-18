def square_numbers(n):
    for i in range(1, n + 1):
        yield i ** 2

gen = square_numbers(5)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))