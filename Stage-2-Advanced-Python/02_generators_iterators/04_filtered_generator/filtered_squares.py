def filtered_squares(n, step):
    while n > 0:
        square = n ** 2
        if square % 2 == 0:
            yield square
        n -= step