def task_filter(n, step):
    while n > 0:
        square = n ** 2
        if square % 2 == 0:
            yield square
        n -= step
        if square < 1000:
            break

for num in task_filter(50, 3):
    print(num)
