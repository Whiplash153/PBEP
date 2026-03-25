def countdown_step(n, step):
    while n > 0:
        yield n ** 2
        n -= step

for num in countdown_step(10, 3):
    print(num)