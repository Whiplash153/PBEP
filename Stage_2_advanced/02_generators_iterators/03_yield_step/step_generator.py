def countdown_step(n, step):
    while n > 0:
        yield n
        n -= step