def square_back_numbers(n):
    for i in range(n, 0, -1):
        yield i ** 2

for num in square_back_numbers(4):
    print(num)