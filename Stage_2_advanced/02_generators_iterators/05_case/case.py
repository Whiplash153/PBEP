class NumberCatalog:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.end:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration

    def even_squares(self):
        for num in range(self.start, self.end + 1):
            square = num ** 2
            if square % 2 == 0:
                yield square

catalog = NumberCatalog(1, 10)

print("All numbers:")
for num in catalog:
    print(num)

print("\nSquares:")
for sq in catalog.even_squares():
    print(sq)

